"""COMMAND : .floodwarn"""

from userbotserbotelethon import events
import asyncio
from userbotserbotollections import deque


@borg.on(events.NewMessage(pattern=r".floodwarn", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("💙💛💓💔💘💕💜💚💝💞💟"))
	for _ in range(100000000):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
