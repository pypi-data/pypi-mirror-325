from typing import Final

from nonebot_plugin_ACMD import CommandFactory
from nonebot import logger

from .perm import AdminManager, AdminType


AP: Final[AdminManager] = AdminManager()

HELP_MSG = """Viv权限配置命令格式：
管理员|黑名单 管理：
   config_viv <add|remove> <super|high|common|black> <PIN> <群组ID>
   示例：config_viv add super admin123 123456"""


@CommandFactory.CLI_cmd_register('config_viv')
async def Viv_perm_handler(arg1: str, arg2: str, arg3: str, arg4: str):
    """
权限配置命令格式：

管理员|黑名单 管理：
   config_viv <add|remove> <super|high|common|black> <PIN> <群组ID>
   示例：config_viv add super admin123 123456
    """
    try:
        args = [arg if arg.lower() != 'none' and arg.lower() != '*' else None for arg in (
            arg1, arg2, arg3, arg4)]
        arg1, arg2, arg3, arg4 = args
        return await handle_admin(arg1, arg2, arg3, arg4)

    except Exception as e:
        logger.error(f"权限配置出错：{str(e)}")
        return f"⚠ 配置失败：{str(e)}"


async def handle_admin(action: str, admin_type_str: str, pin: str, group_id: str) -> str:
    """处理管理员命令"""
    # 参数校验
    if action not in ("add", "remove"):
        return f"无效操作：{action}，请使用add/remove"

    try:
        admin_type = AdminType(admin_type_str.lower())
    except ValueError:
        valid_types = [t.value for t in AdminType]
        return f"无效管理员类型：{admin_type_str}，可用类型：{', '.join(valid_types)}"

    # 执行操作
    try:
        if action == "add":
            await AP.add_admin(admin_type, group_id, pin)
            verb = "添加"
        elif action == 'remove':
            await AP.remove_admin(admin_type, group_id, pin)
            verb = "移除"
        else:
            logger.error('无效操作类型')
            return

        type_map = {
            AdminType.SUPER: "超管",
            AdminType.HIGH: "高管",
            AdminType.COMMON: "管理",
            AdminType.BLACK: "黑名单"
        }
        if admin_type == AdminType.SUPER:
            group_id = '所有群聊'
        logger.success(f"✅ 成功{verb}{type_map[admin_type]} {
                       pin}（群组：{group_id}）")
    except Exception as e:
        logger.error(f"⚠ 操作失败：{str(e)}")
