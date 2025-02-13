import asyncio

from nonebot_plugin_ACMD import CommandFactory, ACMD_get_driver

from .public import ALL_FILES, PIN_POOL
from .members import GroupMembers
from .perm import AdminManager
from .deliver import MsgManager
from .init_files import InitFiles
from .VivHandler import VivMemberRecorder, VivMsgTransmitter
# from .VivCLI import Viv_perm_handler as _

driver = ACMD_get_driver()


@driver.on_startup
async def here_is_VIV():
    await InitFiles.init(ALL_FILES)
    GroupMembers().start()


CommandFactory.create_command(commands=None, handler_list=[
                              VivMemberRecorder(), VivMsgTransmitter()])


@driver.on_shutdown
async def bye():
    tasks = []
    tasks.append(GroupMembers().close())
    tasks.append(MsgManager().close())
    tasks.append(AdminManager().close())
    results = await asyncio.gather(*tasks, return_exceptions=True)
    await PIN_POOL.close()
    exceptions = [i for i in results if isinstance(i, Exception)]
    if exceptions:
        raise exceptions[0]
