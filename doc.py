# by @mrconfused (@sandy1709)

import asyncio
import os
import time
from userbotserbotserbotserbotserbotatetime import datetime
from userbotserbotserbotserbotserboto import BytesIO
from userbotserbotserbotserbotserbotathlib import Path
from userbotserbotserbotserbotserbot import bot as borg
from userbotserbotserbotserbotserbotelethon import functions, types
from userbotserbotserbotserbotserbotelethon.errors import PhotoInvalidDimensionsError
from userbotserbotserbotserbotserbotelethon.errors.rpcerrorlist import YouBlockedUserError
from userbotserbotserbotserbotserbotelethon.tl.functions.messages import SendMediaRequest

from userbotserbotserbotserbotserbotserbot.utils import admin_cmd, progress


if not os.path.isdir("./temp"):
    os.makedirs("./temp")


@borg.on(admin_cmd(pattern="dox ?(.*)"))
async def get(event):
    name = event.text[5:]
    if name is None:
        await event.edit("reply to text message as `.ttf <file name>`")
        return
    m = await event.get_reply_message()
    if m.text:
        with open(name, "w") as f:
            f.write(m.message)
        await event.delete()
        await event.client.send_file(event.chat_id, name, force_document=True)
        os.remove(name)
    else:
        await event.edit("reply to text message as `.ttf <file name>`")

