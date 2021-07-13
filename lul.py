# (c) @UniBorg

from userbotserbotelethon import events
import asyncio
from userbotserbotollections import deque
from userbotserbotniborg.util import admin_cmd

@borg.on(admin_cmd(pattern=r"lul"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("😂🤣😂🤣😂🤣"))
	for _ in range(999):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)