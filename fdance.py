"""Emoji

Available Commands:

.isro

built by @r4v4n4 , isse bhi loot lo betichod"""

from userbotserbotserbotserbotelethon import events

import asyncio

from userbotserbotserbotserbotniborg.util import admin_cmd




@borg.on(admin_cmd(pattern=r"fdance"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 5)

    #input_str = event.pattern_match.group(1)

  #  if input_str == "isro":

    await event.edit("Connecting..")

    animation_chars = [
        
            "⠀⠀⠀⣶⣿⣶/n⠀⠀⠀⣿⣿⣿⣀/n⠀⣀⣿⣿⣿⣿⣿⣿/n⣶⣿⠛⣭⣿⣿⣿⣿/n⠛⠛⠛⣿⣿⣿⣿⠿/n⠀⠀⠀⠀⣿⣿⣿/n⠀⠀⣀⣭⣿⣿⣿⣿⣀/n⠀⠤⣿⣿⣿⣿⣿⣿⠉/n⠀⣿⣿⣿⣿⣿⣿⠉/n⣿⣿⣿⣿⣿⣿/n⣿⣿⣶⣿⣿/n⠉⠛⣿⣿⣶⣤/n⠀⠀⠉⠿⣿⣿⣤/n⠀⠀⣀⣤⣿⣿⣿/n⠀⠒⠿⠛⠉⠿⣿/n⠀⠀⠀⠀⠀⣀⣿⣿/n⠀⠀⠀⠀⣶⠿⠿⠛/n",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤/n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿/n⠀⠀⣶⠀⠀⣀⣤⣶⣤⣉⣿⣿⣤⣀/n⠤⣤⣿⣤⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣀/n⠀⠛⠿⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⠉⠛⠿⣿⣤/n⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⠛⠀⠀⠀⣶⠿/n⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣤⠀⣿⠿/n⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿/n⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⠿⠉⠉/n⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⠿/n⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠉/n⠀⠀⠀⠀⠀⠀⠀⠀⣛⣿⣭⣶⣀/n⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿/n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⣿/n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿/n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⠀⣶⠿/n⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⠿/n⠀⠀⠀⠀⠀⠀⠀⠛⠿⠛/n",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶/n⠀⠀⠀⠀⠀⣀⣀⠀⣶⣿⣿⠶/n⣶⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤/n⠀⠉⠶⣶⣀⣿⣿⣿⣿⣿⣿⣿⠿⣿⣤⣀/n⠀⠀⠀⣿⣿⠿⠉⣿⣿⣿⣿⣭⠀⠶⠿⠿/n⠀⠀⠛⠛⠿⠀⠀⣿⣿⣿⣉⠿⣿⠶/n⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿/n⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠒/n⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⣿/n⠀⠀⠀⠀⠀⣿⣿⣿⠛⣭⣭⠉/n⠀⠀⠀⠀⠀⣿⣿⣭⣤⣿⠛/n⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿⣭/n⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⠿⣶⣤/n⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⣶⣶⠿⠿⠿/n⠀⠀⠀⠀⠀⠀⣿⠛/n⠀⠀⠀⠀⠀⠀⣭⣶/n",
            "⠀⠀⠀⠀⠀⠀⣶⣿⣶/n⠀⠀⠀⣤⣤⣤⣿⣿⣿/n⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣶/n⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿/n⠀⠀⣿⣉⣿⣿⣿⣿⣉⠉⣿⣶/n⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿/n⠀⣤⣿⣿⣿⣿⣿⣿⣿⠿⠀⣿⣶/n⣤⣿⠿⣿⣿⣿⣿⣿⠿⠀⠀⣿⣿⣤/n⠉⠉⠀⣿⣿⣿⣿⣿⠀⠀⠒⠛⠿⠿⠿/n⠀⠀⠀⠉⣿⣿⣿⠀⠀⠀⠀⠀⠀⠉/n⠀⠀⠀⣿⣿⣿⣿⣿⣶/n⠀⠀⠀⠀⣿⠉⠿⣿⣿/n⠀⠀⠀⠀⣿⣤⠀⠛⣿⣿/n⠀⠀⠀⠀⣶⣿⠀⠀⠀⣿⣶/n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿/n⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠉/n",
            "⠀⠀⠀⠀⠀⠀⣤⣶⣶/n⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣀⣀/n⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿/n⣤⣶⣀⠿⠶⣿⣿⣿⠿⣿⣿⣿⣿/n⠉⠿⣿⣿⠿⠛⠉⠀⣿⣿⣿⣿⣿/n⠀⠀⠉⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣤⣤/n⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿/n⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿/n⠀⠀⠀⠀⣀⣿⣿⣿⠿⠉⠀⠀⣿⣿⣿⣿/n⠀⠀⠀⠀⣿⣿⠿⠉⠀⠀⠀⠀⠿⣿⣿⠛/n⠀⠀⠀⠀⠛⣿⣿⣀⠀⠀⠀⠀⠀⣿⣿⣀/n⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠿⣿⣿/n⠀⠀⠀⠀⠀⠉⣿⣿⠀⠀⠀⠀⠀⠀⠉⣿/n⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣀⣿/n⠀⠀⠀⠀⠀⠀⣀⣿⣿/n⠀⠀⠀⠀⠤⣿⠿⠿⠿/n",    


 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 5])
