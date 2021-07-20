#modify by @LEGENDX22
#credits shivam thanks bruh

from userbotserbotserbotserbotelethon import events
from userbotserbotserbotserbotserbot.events import remove_plugin, load_module
from userbotserbotserbotserbotelethon import functions, types
from userbotserbotserbotserbotelethon.tl.types import InputMessagesFilterDocument
from userbotserbotserbotserbotserbot.utils import command, remove_plugin, load_module
from userbotserbotserbotserbotathlib import Path
from userbotserbotserbotserbot import LOAD_PLUG, CMD_HELP
from userbotserbotserbotserbotserbot.utils import admin_cmd
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
