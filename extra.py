import asyncio, subprocess
import time, re, io
from . import bot, BOTLOG, BOTLOG_CHATID, CmdHelp
from telethon import events, functions, types
from telethon.events import StopPropagation
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.channels import LeaveChannelRequest, CreateChannelRequest, DeleteMessagesRequest
from collections import deque
from telethon.tl.functions.users import GetFullUserRequest
from userbot.events import register
from userbot.utils import admin_cmd


@borg.on(admin_cmd(";__;$"))
#@register(outgoing=True, pattern="^;__;$")
async def fun(e):
    t = ";__;"
    for j in range(10):
        t = t[:-1] + "_;"
        await e.edit(t)

@borg.on(admin_cmd("yo$"))
#@register(outgoing=True, pattern="^yo$")
async def Ooo(e):
    t = "yo"
    for j in range(15):
        t = t[:-1] + "oo"
        await e.edit(t)

@borg.on(admin_cmd("Oof$"))
#@register(outgoing=True, pattern="^Oof$")
async def Oof(e):
    t = "Oof"
    for j in range(15):
        t = t[:-1] + "of"
        await e.edit(t)

@borg.on(admin_cmd("ccry$"))
#@register(outgoing=True, pattern="^.cry$")
async def cry(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(;´༎ຶД༎ຶ)")

@borg.on(admin_cmd("fp$"))
#@register(outgoing=True, pattern="^.fp$")
async def facepalm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("🤦‍♂")

@borg.on(admin_cmd("moon$"))
#@register(outgoing=True, pattern="^.mmoon$")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
		

@borg.on(admin_cmd("source$"))
#@register(outgoing=True, pattern="^.source$")
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("/HellBoy-OP/LEGENDBOT")

@borg.on(admin_cmd("readme$"))
#@register(outgoing=True, pattern="^.readme$")
async def reedme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("/HellBoy-OP/LEGENDBOT/blob/master/README.md")


@borg.on(admin_cmd(pattern="evil ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("😒You Know I'm a good **PERSON**😏")
        await asyncio.sleep(1.9)
        await event.edit("BUT😡")
        await asyncio.sleep(1.2)
        await event.edit("😑Don't give me a reason😠")
        await asyncio.sleep(1.9)
        await event.edit("🤨To show my😎")
        await asyncio.sleep(1.4)
        await event.edit("**😈EVIL SIDE**😈")
        await asyncio.sleep(1.3)
        await event.edit("**😈YOU KNOW THAT I'M A GOOD PERSON. BUT DON'T GIVE ME REASON TO SHOW MY EVIL SIDE😈**")



@borg.on(admin_cmd("heart$"))		
#@register(outgoing=True, pattern="^.heart$")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("❤️🧡💛💚💙💜🖤"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
		
@borg.on(admin_cmd("fap$"))
#@register(outgoing=True, pattern="^.fap$")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🍆✊🏻💦"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)




CmdHelp.update({
    ";__;": "You try it!"
})
CmdHelp.update({
    "evil": "Evil Guy"
})
CmdHelp.update({
    "cry": "Cry"
})
CmdHelp.update({
    "fp": "Send face palm emoji."
})
CmdHelp.update({
    "moon": "Bot will send a cool moon animation."
})
CmdHelp.update({
    "clock": "Bot will send a cool clock animation."
})
CmdHelp.update({
    "readme": "Reedme."
})
CmdHelp.update({
    "source": "Gives the source of your userbot"
})
CmdHelp.update({
    "myusernames": "List of Usernames owned by you."
})
CmdHelp.update({
    "oof": "Same as ;__; but ooof"
})
CmdHelp.update({
    "earth": "Sends Kensar Earth animation"
})
CmdHelp.update({
    "heart": "Try and you'll get your emotions back"
})
CmdHelp.update({
    "fap": "Faking orgasm"
})
