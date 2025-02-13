import os
import asyncio
import aiosqlite
import aiofiles
import aiofiles.os
from nonebot import logger
from typing import List, Dict, Awaitable


async def PIN_init(path: str):
    logger.info('检查数据库...')

    async def ensure_table(conn: aiosqlite.Connection, table_def: Dict):
        async with conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=:name",
            {'name': table_def['name']}
        ) as cursor:
            if not await cursor.fetchone():
                columns = [' '.join(col).strip()
                           for col in table_def['columns']]
                await conn.execute(f"CREATE TABLE {table_def['name']} ({', '.join(columns)})")
                return

        async with conn.execute(f"PRAGMA table_info({table_def['name']})") as cursor:
            existing_columns = {row[1] for row in await cursor.fetchall()}

        for col in table_def['columns']:
            if (col_name := col[0]) not in existing_columns:
                await conn.execute(f"ALTER TABLE {table_def['name']} ADD COLUMN {col_name} {' '.join(col[1:])}")

    async def ensure_indexes(conn: aiosqlite.Connection, table_def: Dict):
        for idx_name, idx_col in table_def.get('indexes', []):
            async with conn.execute(
                "SELECT name FROM sqlite_master WHERE type='index' AND name=:name",
                {'name': idx_name}
            ) as cursor:
                if not await cursor.fetchone():
                    await conn.execute(f"CREATE INDEX {idx_name} ON {table_def['name']}({idx_col})")

    try:
        async with aiosqlite.connect(path) as conn:
            await conn.execute("PRAGMA journal_mode=WAL")
            tables = [
                {
                    'name': 'PIN_love',
                    'columns': [
                        ('PIN', 'TEXT', 'PRIMARY KEY'),
                        ('currency', 'INTEGER', 'DEFAULT 0'),
                        ('love', 'INTEGER', 'DEFAULT 0'),
                        ('alias', 'TEXT', 'DEFAULT ""'),
                        ('extra', 'TEXT', 'DEFAULT ""'),
                        ('pic', 'BLOB'),
                        ('real_id', 'TEXT', 'UNIQUE'),
                        ('state', 'INTEGER', 'DEFAULT 200')
                    ],
                    'indexes': [
                        ('idx_real_id', 'real_id'),
                        ('idx_alias', 'alias'),
                        ('idx_love', 'love'),
                        ('idx_PIN', 'PIN')
                    ]
                },
                {
                    'name': 'code',
                    'columns': [
                        ('code', 'TEXT', 'PRIMARY KEY'),
                        ('userid', 'TEXT', 'DEFAULT ""'),
                        ('count', 'INTEGER', 'DEFAULT 5'),
                        ('type', 'TEXT', 'DEFAULT alias')
                    ],
                    'indexes': [
                        ('idx_code_code', 'code'),
                        ('idx_code_userid', 'userid'),
                        ('idx_code_type', 'type')
                    ]
                }
            ]

            for table in tables:
                await ensure_table(conn, table)
                await ensure_indexes(conn, table)

            # 释放空间并整理索引
            await conn.execute("VACUUM")
            await conn.execute("REINDEX")

            await conn.commit()

    except aiosqlite.Error as e:
        logger.critical(f"数据库初始化失败: {e}")
        raise

    logger.info('数据库检查完成')


class InitFiles:
    db_init_map: Dict[str, Awaitable] = {
        'PIN.db3': PIN_init
    }

    @classmethod
    async def init(cls, path_list: List[str]):
        tasks = set()
        later_tasks = []
        for path in path_list:
            dir_name = os.path.dirname(path)
            if dir_name:
                tasks.add(aiofiles.os.makedirs(dir_name, exist_ok=True))
            if path.endswith('.db3'):
                later_tasks.append(
                    cls.db_init_map[os.path.basename(path)](path))
        await asyncio.gather(*tasks)
        await asyncio.gather(*later_tasks)
