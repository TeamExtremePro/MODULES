# (c) @UniBorg

from userbotserbotserbotserbotserbotelethon import events
import asyncio
from userbotserbotserbotserbotserbotollections import deque
from userbotserbotserbotserbotserbotniborg.util import admin_cmd

@borg.on(admin_cmd(pattern=r"moon", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
