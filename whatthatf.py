from userbotserbotserbotserbotelethon import events
import asyncio
import os
import sys
from userbotserbotserbotserbotelethon import events, functions, __version__
from userbotserbotserbotserbotniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="f"))
async def payf(event):
    paytext=event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(paytext*8, paytext*8, paytext*2, paytext*2, paytext*2, paytext*6, paytext*6, paytext*2, paytext*2, paytext*2, paytext*2, paytext*2)
    await event.edit(pay)
