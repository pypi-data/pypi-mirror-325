import os
import json
import asyncio
import heapq
import aiofiles
from datetime import datetime, timedelta
from typing import Optional, Dict, Tuple

from nonebot import logger
from nonebot.adapters.onebot.v11 import Bot, MessageEvent

from .public import DELIVER_JSON, singleton


@singleton
class MsgManager:
    __slots__ = ['filename', 'specific_entries', 'user_wildcards',
                 'group_wildcards', 'global_wildcard', 'lock',
                 'notice_heap', 'notice_info', '_save_pending', '_closed']

    def __init__(self, filename: str = DELIVER_JSON):
        self.filename = filename
        self.specific_entries: Dict[Tuple[int, int], Dict] = {}
        self.user_wildcards: Dict[int, Dict] = {}
        self.group_wildcards: Dict[int, Dict] = {}
        self.global_wildcard: Optional[Dict] = None
        self.notice_heap: list = []  # 堆结构 (expire_time, content)
        # content: {groups: Set[int], expire_time: datetime}
        self.notice_info: Dict[str, Dict] = {}
        self.lock = asyncio.Lock()
        self._save_pending = False  # 延迟保存标记
        self._closed = False
        if asyncio._get_running_loop():
            asyncio.create_task(self.load_data()).result()
        else:
            asyncio.run(self.load_data())

    async def load_data(self):
        """异步加载数据"""
        async with self.lock:
            if not os.path.exists(self.filename):
                return

            try:
                async with aiofiles.open(self.filename, 'r', encoding='utf-8') as f:
                    raw_data = json.loads(await f.read())

                # 清空现有数据
                self.specific_entries.clear()
                self.user_wildcards.clear()
                self.group_wildcards.clear()
                self.global_wildcard = None
                self.notice_heap.clear()
                self.notice_info.clear()

                current_time = datetime.now()

                # 加载通知
                if "NOTICES" in raw_data:
                    for content, data in raw_data["NOTICES"].items():
                        expire_time = datetime.fromisoformat(
                            data["expire_time"])
                        if expire_time > current_time:
                            heapq.heappush(self.notice_heap,
                                           (expire_time, content))
                            self.notice_info[content] = {
                                "groups": set(data["groups"]),
                                "expire_time": expire_time
                            }

                # 加载其他消息类型
                for key, value in raw_data.items():
                    if key == "WILDCARD":
                        self.global_wildcard = value
                    elif key == "NOTICES":
                        continue
                    else:
                        pin_part, gid_part = key.split(':', 1)
                        pin = None if pin_part == '*' else int(pin_part)
                        gid = None if gid_part == '*' else int(gid_part)

                        if pin is not None and gid is not None:
                            self.specific_entries[(pin, gid)] = value
                        elif pin is not None:
                            self.user_wildcards[pin] = value
                        elif gid is not None:
                            self.group_wildcards[gid] = value

            except Exception as e:
                logger.error(f"消息传递数据加载失败: {e}")

    async def _schedule_save(self):
        """延迟保存调度"""
        if self._closed or self._save_pending:
            return
        self._save_pending = True
        await asyncio.sleep(1)
        async with self.lock:
            if self._closed:
                self._save_pending = False
                return
            save_data = self._generate_save_data()
        self._save_pending = False
        await self._do_save(save_data)

    def _generate_save_data(self) -> dict:
        """生成需要保存的数据结构（需在锁内调用）"""
        save_data = {}

        # 保存通知
        notices_data = {}
        for content, info in self.notice_info.items():
            notices_data[content] = {
                "groups": list(info["groups"]),
                "expire_time": info["expire_time"].isoformat()
            }
        if notices_data:
            save_data["NOTICES"] = notices_data

        # 保存其他消息类型
        for (pin, gid), data in self.specific_entries.items():
            if data['times'] > 0:
                save_data[f"{pin}:{gid}"] = data

        for pin, data in self.user_wildcards.items():
            if data['times'] > 0:
                save_data[f"{pin}:*"] = data

        for gid, data in self.group_wildcards.items():
            if data['times'] > 0:
                save_data[f"*:{gid}"] = data

        if self.global_wildcard and self.global_wildcard['times'] > 0:
            save_data["WILDCARD"] = self.global_wildcard

        return save_data

    async def _do_save(self, save_data: dict):
        """实际执行保存操作（无需持有锁）"""
        try:
            async with aiofiles.open(self.filename, 'w', encoding='utf-8') as f:
                await f.write(json.dumps(save_data, ensure_ascii=False, indent=2))
        except Exception as e:
            logger.error(f"数据保存失败: {e}")

    async def set_message(
        self,
        content: str,
        PIN: Optional[int] = None,
        groupid: Optional[int] = None,
        times: int = 1
    ):
        """设置消息"""
        async with self.lock:
            msg_data = {"content": content, "times": times}

            if PIN is not None and groupid is not None:
                self.specific_entries[(PIN, groupid)] = msg_data
            elif PIN is not None:
                self.user_wildcards[PIN] = msg_data
            elif groupid is not None:
                self.group_wildcards[groupid] = msg_data
            else:
                self.global_wildcard = msg_data

        await self._schedule_save()

    async def set_notice(self, content: str, expire_days: int = 7):
        """设置通知（默认7天有效期）"""
        async with self.lock:
            if content not in self.notice_info:
                expire_time = datetime.now() + timedelta(days=expire_days)
                heapq.heappush(self.notice_heap, (expire_time, content))
                self.notice_info[content] = {
                    "groups": set(),
                    "expire_time": expire_time
                }
        await self._schedule_save()

    async def get_notice(self, groupid: int) -> Optional[str]:
        """获取指定群组应接收的通知"""
        async with self.lock:
            current_time = datetime.now()

            # 清理过期通知
            while self.notice_heap:
                expire_time, content = self.notice_heap[0]
                if expire_time > current_time:
                    break
                heapq.heappop(self.notice_heap)
                if content in self.notice_info:
                    del self.notice_info[content]

            # 查找未发送的通知
            for content in list(self.notice_info.keys()):
                info = self.notice_info[content]
                if groupid not in info["groups"]:
                    info["groups"].add(groupid)
                    await self._schedule_save()
                    return content
            return None

    async def get_message(
        self,
        PIN: Optional[int] = None,
        groupid: Optional[int] = None
    ) -> Optional[str]:
        """获取匹配的消息"""
        async with self.lock:
            check_order = []
            if PIN is not None and groupid is not None:
                check_order.append(self.specific_entries.get((PIN, groupid)))
            if PIN is not None:
                check_order.append(self.user_wildcards.get(PIN))
            if groupid is not None:
                check_order.append(self.group_wildcards.get(groupid))
            check_order.append(self.global_wildcard)

            for data in check_order:
                if not data or data['times'] <= 0:
                    continue

                data['times'] -= 1
                content = data['content']

                # 自动清理过期消息
                if data['times'] <= 0:
                    if data is self.global_wildcard:
                        self.global_wildcard = None
                    else:
                        # 需要确定具体位置进行删除
                        for key, value in self.specific_entries.items():
                            if value is data:
                                del self.specific_entries[key]
                                break
                        else:
                            for key, value in self.user_wildcards.items():
                                if value is data:
                                    del self.user_wildcards[key]
                                    break
                            else:
                                for key, value in self.group_wildcards.items():
                                    if value is data:
                                        del self.group_wildcards[key]
                                        break

                await self._schedule_save()
                return content
            return None

    async def send(self, bot: Bot, event: MessageEvent,
                   PIN: Optional[int] = None, groupid: Optional[int] = None) -> bool:
        """综合发送方法"""
        # 优先发送群组通知
        if groupid is not None:
            if content := await self.get_notice(groupid):
                await bot.send(event, f"通知：\n{content}")
                return True

        # 发送消息
        if content := await self.get_message(PIN, groupid):
            await bot.send(event, f"主人留言：\n{content}")
            return True

        return False

    async def close(self):
        """确保所有数据保存"""
        async with self.lock:
            if self._closed:
                return
            self._closed = True
            save_data = self._generate_save_data()
        await self._do_save(save_data)
