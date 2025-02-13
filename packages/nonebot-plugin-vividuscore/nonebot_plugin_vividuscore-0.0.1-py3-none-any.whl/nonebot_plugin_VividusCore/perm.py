import asyncio
import json
from enum import Enum
from typing import Dict, List, Optional, Any, Union

import aiofiles
from nonebot import logger

from .public import ADMIN_JSON, singleton


class AdminType(str, Enum):
    """管理员类型枚举"""

    def __new__(cls, value, priority):
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.priority = priority
        return obj

    SUPER = ('super', 3)
    """BOT超管"""
    HIGH = ('high', 2)
    """群聊高管"""
    COMMON = ('common', 1)
    """群聊管理"""
    BLACK = ('black', -1)
    """黑名单"""


class VivPermission:
    __slots__ = ('permission')

    def __init__(self, permission: Union[AdminType, None]):
        self.permission = permission

    def has_permission(self, required: Union[AdminType, None]) -> bool:
        if self.permission == AdminType.BLACK:
            return False
        return self._get_priority() >= (required.priority if required else 0)

    def _get_priority(self) -> int:
        return self.permission.priority if self.permission else 0

    def __eq__(self, other):
        if not isinstance(other, VivPermission):
            return NotImplemented
        return self._get_priority() == other._get_priority()

    def __lt__(self, other):
        if not isinstance(other, VivPermission):
            return NotImplemented
        return self._get_priority() < other._get_priority()

    def __le__(self, other):
        if not isinstance(other, VivPermission):
            return NotImplemented
        return self._get_priority() <= other._get_priority()

    def __gt__(self, other):
        if not isinstance(other, VivPermission):
            return NotImplemented
        return self._get_priority() > other._get_priority()

    def __ge__(self, other):
        if not isinstance(other, VivPermission):
            return NotImplemented
        return self._get_priority() >= other._get_priority()


@singleton
class AdminManager:
    __slots__ = ('filename', 'lock', '_save_handle', 'admin_data')

    def __init__(self, filename: str = ADMIN_JSON) -> None:
        self.filename = filename
        self.lock = asyncio.Lock()
        self._save_handle: Optional[asyncio.TimerHandle] = None
        self.admin_data = self._load_data()

    def _load_data(self) -> Dict[str, Any]:
        """加载数据并初始化黑名单结构"""
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)

            return data
        except FileNotFoundError:
            return self._default_data()
        except json.JSONDecodeError:
            logger.error("管理员文件损坏，已重置")
            return self._default_data()

    def _default_data(self) -> Dict[str, Any]:
        return {
            'groups': {},
            'super': set(),
            'blacklist': {
                'pins': set(),
                'groups': set(),
                'group_pins': {}
            }
        }

    async def _save(self):
        async with self.lock:
            dump_data = {
                'groups': {
                    gid: {t: list(pins) for t, pins in types.items()}
                    for gid, types in self.admin_data['groups'].items()
                },
                'super': list(self.admin_data['super']),
                'blacklist': {
                    'pins': list(self.admin_data['blacklist']['pins']),
                    'groups': list(self.admin_data['blacklist']['groups']),
                    'group_pins': {
                        gid: list(pins)
                        for gid, pins in self.admin_data['blacklist']['group_pins'].items()
                    }
                }
            }
            async with aiofiles.open(self.filename, 'w') as f:
                await f.write(json.dumps(dump_data, ensure_ascii=False))

    async def _debounced_save(self) -> None:
        """防抖保存"""
        if self._save_handle:
            self._save_handle.cancel()

        loop = asyncio.get_running_loop()
        self._save_handle = loop.call_later(
            1, lambda: asyncio.create_task(self._save()))

    async def add_admin(self, admin_type: AdminType, group_id: str = None, PIN: str = None) -> None:
        """添加管理员"""
        if admin_type == AdminType.SUPER:
            if PIN not in self.admin_data['super']:
                self.admin_data['super'].add(PIN)
                await self._debounced_save()
            return
        if admin_type == AdminType.BLACK:
            return await self._handle_blacklist(PIN, group_id, add=True)

        group = self.admin_data['groups'].setdefault(
            group_id, {'high': set(), 'common': set()})
        target = group[admin_type.value]
        if PIN not in target:
            target.add(PIN)
            await self._debounced_save()

    async def remove_admin(self, admin_type: AdminType, group_id: str = None, PIN: str = None) -> None:
        """移除管理员"""
        if admin_type == AdminType.SUPER:
            if PIN in self.admin_data['super']:
                self.admin_data['super'].remove(PIN)
                await self._debounced_save()
            return
        if admin_type == AdminType.BLACK:
            return await self._handle_blacklist(PIN, group_id, add=False)

        if group_id in self.admin_data['groups']:
            group = self.admin_data['groups'][group_id]
            if PIN in group.get(admin_type.value, set()):
                group[admin_type.value].remove(PIN)
                await self._debounced_save()

    async def _handle_blacklist(self, PIN: Optional[str], group_id: Optional[str], add: bool) -> None:
        """统一处理黑名单操作"""
        has_pin = PIN is not None and PIN.strip() != ""
        has_group = group_id is not None and group_id.strip() != ""

        if not has_pin and not has_group:
            raise ValueError("必须提供PIN或群组ID")

        bl_data = self.admin_data['blacklist']
        changed = False

        if has_pin and has_group:
            # 处理特定群组的封禁
            group_pins = bl_data['group_pins'].setdefault(group_id, set())
            if add:
                if PIN not in group_pins:
                    group_pins.add(PIN)
                    changed = True
            else:
                if group_id in bl_data['group_pins'] and PIN in group_pins:
                    group_pins.remove(PIN)
                    if not group_pins:
                        del bl_data['group_pins'][group_id]
                    changed = True
        elif has_pin:
            # 全局封禁用户
            if add:
                if PIN not in bl_data['pins']:
                    bl_data['pins'].add(PIN)
                    changed = True
            else:
                if PIN in bl_data['pins']:
                    bl_data['pins'].remove(PIN)
                    changed = True
        else:
            # 封禁整个群组
            if add:
                if group_id not in bl_data['groups']:
                    bl_data['groups'].add(group_id)
                    changed = True
            else:
                if group_id in bl_data['groups']:
                    bl_data['groups'].remove(group_id)
                    changed = True

        if changed:
            await self._debounced_save()

    def is_blacked(self, *, pin: Optional[str] = None, group_id: Optional[str] = None) -> bool:
        """检查黑名单状态"""
        bl = self.admin_data['blacklist']

        if pin:
            # 全局封禁检查
            if pin in bl['pins']:
                return True

            # 特定群组封禁检查
            if group_id and group_id in bl['group_pins']:
                return pin in bl['group_pins'][group_id]

        if group_id:
            # 群组全局封禁检查
            return group_id in bl['groups']

        return False

    def get_admin_type(self, group_id: str, PIN: str) -> VivPermission:
        """权限检查"""
        # 优先检查黑名单
        if self.is_blacked(pin=PIN):
            return VivPermission(AdminType.BLACK)
        if self.is_blacked(group_id=group_id):
            return VivPermission(AdminType.BLACK)

        # 原有权限判断逻辑
        admin_type = None
        if PIN in self.admin_data['super']:
            admin_type = AdminType.SUPER
        elif group_id in self.admin_data['groups']:
            group = self.admin_data['groups'][group_id]
            if PIN in group['high']:
                admin_type = AdminType.HIGH
            elif PIN in group['common']:
                admin_type = AdminType.COMMON
        return VivPermission(admin_type)

    def list_admins(self, group_id: Optional[str] = None, admin_type: Optional[AdminType] = None) -> List[str]:
        """列表查询"""
        if admin_type == AdminType.SUPER:
            return list(self.admin_data['super']) if group_id is None else []

        if group_id is None:
            return []

        group = self.admin_data['groups'].get(group_id, {})
        if admin_type:
            return list(group.get(admin_type.value, []))
        return list(group.get('high', [])) + list(group.get('common', []))

    def list_blacklist(self) -> Dict[str, Union[List[str], Dict[str, List[str]]]]:
        """获取完整黑名单信息"""
        bl = self.admin_data['blacklist']
        return {
            'global_pins': list(bl['pins']),
            'banned_groups': list(bl['groups']),
            'group_bans': {
                gid: list(pins)
                for gid, pins in bl['group_pins'].items()
            }
        }

    async def close(self):
        """
        关闭AdminManager
        """
        if self._save_handle:
            self._save_handle.cancel()
        await self._save()
