"""
公共模块,应该避免导入其他模块.
"""
import os
import threading
from typing import Final, List
from functools import wraps

from nonebot import require, logger
from nonebot_plugin_ACMD.connection_pool import SQLitePool

require("nonebot_plugin_localstore")

import nonebot_plugin_localstore  # noqa

ALL_FILES: List[str] = []
DATA_DIR: Final[str] = str(
    nonebot_plugin_localstore.get_data_dir("nonebot_plugin_VividusCore"))
logger.info(f'nonebot_plugin_VividusCore 的数据目录位于 {DATA_DIR}')


def singleton(cls):
    """单例模式装饰器"""
    instances = {}
    lock = threading.Lock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with lock:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper


PIN_PATH: Final[str] = os.path.join(DATA_DIR, 'DataBase', 'users', 'PIN.db3')
ALL_FILES.append(PIN_PATH)

PIN_POOL: Final[SQLitePool] = SQLitePool(db_file=PIN_PATH, max_size=10)

DELIVER_JSON: Final[str] = os.path.join(
    DATA_DIR, 'json', 'Msg_Transmitter.json')
ALL_FILES.append(DELIVER_JSON)

ADMIN_JSON: Final[str] = os.path.join(DATA_DIR, 'json', 'admins.json')
ALL_FILES.append(ADMIN_JSON)
