from typing import Final

from nonebot_plugin_ACMD import BasicHandler, CommandFactory
from nonebot_plugin_ACMD.Atypes import PIN, GroupID, HandlerContext
from nonebot.adapters.onebot.v11 import Bot, MessageEvent

from .members import GroupMembers
from .perm import AdminManager, VivPermission
from .deliver import MsgManager


AP: Final[AdminManager] = AdminManager()


@CommandFactory.parameter_injection('VivPermission', VivPermission)
async def AdminPermission(context: HandlerContext):
    return AP.get_admin_type(context.groupid.str, context.pin.user)


class VivMemberRecorder(BasicHandler):

    __slots__ = [slot for slot in BasicHandler.__slots__ if slot !=
                 '__weakref__'] + ['GM']

    def __init__(self, block: bool = True, unique: str = None):
        super().__init__(block=block, unique=unique)
        self.GM: Final[GroupMembers] = GroupMembers()

    async def handle(self, PIN: PIN, groupid: GroupID):
        await self.GM.create_and_insert_if_not_exists(groupid.str, PIN.user)

    async def should_block(self):
        return False


class VivMsgTransmitter(BasicHandler):

    __slots__ = [slot for slot in BasicHandler.__slots__ if slot !=
                 '__weakref__'] + ['Msg']

    def __init__(self, block: bool = True, unique: str = None):
        super().__init__(block=block, unique=unique)
        self.Msg: Final[MsgManager] = MsgManager()

    async def handle(self, bot: Bot, event: MessageEvent, PIN: PIN, groupid: GroupID):
        await self.Msg.send(bot, event, int(PIN.user), groupid.int)

    async def should_block(self):
        return False
