import aiosqlite
import asyncio
import time
from contextlib import asynccontextmanager
from collections import defaultdict
from typing import AsyncGenerator, List

from nonebot import logger

from .public import PIN_POOL, singleton


@singleton
class GroupMembers:
    """基于队列的定时群成员管理"""

    __slots__ = ['pool', 'checked_tables', 'write_queue',
                 'batch_task', 'cleanup_task', '_shutdown']

    def __init__(self, pool=PIN_POOL):
        self.pool = pool
        self.checked_tables = set()
        self.write_queue = asyncio.Queue()
        self.batch_task = None
        self.cleanup_task = None
        self._shutdown = False

    def start(self):
        """启动定时任务"""
        self.batch_task = asyncio.create_task(self._batch_writer())
        self.cleanup_task = asyncio.create_task(self._cleanup())

    async def _batch_writer(self):
        """5秒队列处理器"""
        while not self._shutdown:
            batch_data = defaultdict(list)

            try:
                while True:
                    try:
                        groupid, userid = await asyncio.wait_for(
                            self.write_queue.get(),
                            timeout=5
                        )
                        batch_data[groupid].append(userid)
                    except asyncio.TimeoutError:
                        break
            except asyncio.CancelledError:
                break

            if batch_data:
                conn = await self.pool.acquire()
                try:
                    async with self._transaction(conn):
                        for groupid, users in batch_data.items():
                            table_name = f"PIN_{groupid}"
                            await self._ensure_table(conn, groupid)
                            await conn.executemany(
                                f'''INSERT INTO "{table_name}" (PIN, last_updated)
                                VALUES (?, ?)
                                ON CONFLICT(PIN) DO UPDATE SET last_updated=excluded.last_updated''',
                                [(uid, int(time.time())) for uid in users]
                            )
                finally:
                    await self.pool.release(conn)

    async def _cleanup(self):
        """30分钟清理任务"""
        while not self._shutdown:

            conn = await self.pool.acquire()
            try:
                async with self._transaction(conn):
                    seven_days_ago = int(time.time()) - 7 * 86400
                    cursor = await conn.execute(
                        "SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'PIN_%' AND name != 'PIN_love'"
                    )
                    async for row in cursor:
                        await conn.execute(
                            f'DELETE FROM "{row[0]}" WHERE last_updated < ?',
                            (seven_days_ago,)
                        )
            except asyncio.CancelledError:
                break
            finally:
                await self.pool.release(conn)
                logger.info("完成一次用户数据清洗")

            await asyncio.sleep(1800)

    async def _ensure_table(self, conn: aiosqlite.Connection, groupid: int):
        """表结构优化（带索引）"""
        table_name = f"PIN_{groupid}"
        if table_name not in self.checked_tables:
            await conn.execute(
                f'''CREATE TABLE IF NOT EXISTS "{table_name}" (
                    PIN TEXT PRIMARY KEY,
                    last_updated INTEGER NOT NULL
                )'''
            )
            await conn.execute(
                f'CREATE INDEX IF NOT EXISTS "idx_{
                    table_name}_ts" ON "{table_name}"(last_updated)'
            )
            self.checked_tables.add(table_name)

    @asynccontextmanager
    async def _transaction(self, conn: aiosqlite.Connection) -> AsyncGenerator[None, None]:
        """事务管理"""
        await conn.execute("BEGIN")
        try:
            yield
            await conn.commit()
        except:
            await conn.rollback()
            raise

    async def create_and_insert_if_not_exists(self, groupid: int, userid: str):
        """无锁写入队列"""
        logger.debug(f'{groupid}-{userid}加入记录队列')
        await self.write_queue.put((groupid, userid))

    async def get_top_users_by_groupid(self, groupid: int) -> List[str]:
        """查询"""
        conn = await self.pool.acquire()
        try:
            table_name = f"PIN_{groupid}"
            async with conn.execute(
                f'''SELECT t1.PIN
                FROM PIN_love AS t1
                JOIN "{table_name}" AS t2 ON t1.PIN = t2.PIN
                ORDER BY t1.love DESC
                LIMIT 10'''
                ) as cursor:
                return [row[0] async for row in cursor]
        finally:
            await self.pool.release(conn)

    async def close(self):
        """安全关闭流程"""
        self._shutdown = True

        # 取消任务
        if self.batch_task:
            self.batch_task.cancel()
            await self.batch_task
        if self.cleanup_task:
            self.cleanup_task.cancel()
            await self.cleanup_task

        # 处理剩余数据
        if not self.write_queue.empty():
            conn = await self.pool.acquire()
            try:
                batch_data = defaultdict(list)
                while not self.write_queue.empty():
                    groupid, userid = await self.write_queue.get()
                    batch_data[groupid].append(userid)

                async with self._transaction(conn):
                    for groupid, users in batch_data.items():
                        table_name = f"PIN_{groupid}"
                        await self._ensure_table(conn, groupid)
                        await conn.executemany(
                            f"""INSERT INTO {table_name} (PIN, last_updated)
                                VALUES (?, ?)
                                ON CONFLICT(PIN) DO UPDATE SET last_updated=excluded.last_updated""",
                            [(uid, int(time.time()))
                             for uid in users]
                        )
            finally:
                await self.pool.release(conn)
