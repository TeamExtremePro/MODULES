from userbotelethon import events
import asyncio
import os
import sys
from userbotelethon import events, functions, __version__
from userbotniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="f"))
async def payf(event):
    paytext=event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(paytext*8, paytext*8, paytext*2, paytext*2, paytext*2, paytext*6, paytext*6, paytext*2, paytext*2, paytext*2, paytext*2, paytext*2)
    await event.edit(pay)
