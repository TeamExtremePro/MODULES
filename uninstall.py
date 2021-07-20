#modify by @LEGENDX22
#credits shivam thanks bruh

from userbotserbotserbotelethon import events
from userbotserbotserbotserbot.events import remove_plugin, load_module
from userbotserbotserbotelethon import functions, types
from userbotserbotserbotelethon.tl.types import InputMessagesFilterDocument
from userbotserbotserbotserbot.utils import command, remove_plugin, load_module
from userbotserbotserbotathlib import Path
from userbotserbotserbot import LOAD_PLUG, CMD_HELP
from userbotserbotserbotserbot.utils import admin_cmd
import os
@bot.on(admin_cmd(pattern=r"^uninstall (?P<shortname>\w+)$"))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    dir_path =f"./userbot/plugins/{shortname}.py"
    try:
        remove_plugin(shortname)
        os.remove(dir_path)
        await event.edit(f"Uninstalled {shortname} successfully")
    except OSError as e:
        await event.edit("Error: %s : %s" % (dir_path, e.strerror))

CMD_HELP.update(
    {
        "uninstall": "**Plugin : **`uninstall`\
    \n\n**Syntax : **`uninstall`\
    \n**Function : **use this plugin without . and small later"
    }
)
