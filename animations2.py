import asyncio
from userbotserbotserbotserbotserbotollections import deque

from userbotserbotserbotserbotserbotserbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbotserbotserbotserbotserbot import ALIVE_NAME, CMD_HELP

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"


@bot.on(admin_cmd(pattern=r"boxs$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"boxs$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "`boxs...`")
    deq = deque(list("π₯π§π¨π©π¦πͺπ«β¬β¬"))
    for _ in range(999):
        await asyncio.sleep(0.3)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"rain$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"rain$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "`Raining.......`")
    deq = deque(list("π¬βοΈπ©π¨π§π¦π₯βπ€"))
    for _ in range(48):
        await asyncio.sleep(0.3)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"deploy$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"deploy$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(12)
    event = await edit_or_reply(event, "`Deploying...`")
    animation_chars = [
     "**Heroku Connecting To Latest [Github Build](HellBoy-OP/LEGENDBOT)**",
            f"**Build started by user** {DEFAULTUSER}",
            f"**Deploy** `535a74f0` **by user** **{DEFAULTUSER}**",
            "**Restarting Heroku Server...**",
            "**State changed from userbotserbotserbotserbotserbotp to starting**",    
            "**Stopping all processes with SIGTERM**",
            "**Process exited with** `status 143`",
            "**Starting process with command** `python3 -m stdborg`",
            "**State changed from userbotserbotserbotserbotserbottarting to up**",
            "__INFO:HΓͺllαΊΓΈβ :Logged in as 557667062__",
            "__INFO:HΓͺllαΊΓΈβ :Successfully loaded all plugins__",
            "**Build Succeeded**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])


@bot.on(admin_cmd(pattern=r"dump$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"dump$", allow_sudo=True))
async def _(message):
    if event.fwd_from:
        return
    try:
        obj = message.pattern_match.group(1)
        if len(obj) != 3:
            raise IndexError
        inp = " ".join(obj)
    except IndexError:
        inp = "π₯ π π«"
    event = await edit_or_reply(message, "`droping....`")
    u, t, g, o, s, n = inp.split(), "π", "<(^_^ <)", "(> ^_^)>", "β  ", "\n"
    h = [(u[0], u[1], u[2]), (u[0], u[1], ""), (u[0], "", "")]
    for something in reversed(
        [
            y
            for y in (
                [
                    "".join(x)
                    for x in (
                        f + (s, g, s + s * f.count(""), t),
                        f + (g, s * 2 + s * f.count(""), t),
                        f[:i] + (o, f[i], s * 2 + s * f.count(""), t),
                        f[:i] + (s + s * f.count(""), o, f[i], s, t),
                        f[:i] + (s * 2 + s * f.count(""), o, f[i], t),
                        f[:i] + (s * 3 + s * f.count(""), o, t),
                        f[:i] + (s * 3 + s * f.count(""), g, t),
                    )
                ]
                for i, f in enumerate(reversed(h))
            )
        ]
    ):
        for something_else in something:
            await asyncio.sleep(0.3)
            try:
                await event.edit(something_else)
            except errors.MessageIdInvalidError:
                return


@bot.on(admin_cmd(pattern=r"fleaveme$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"fleaveme$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(10)
    animation_chars = [
        "β¬β¬β¬\nβ¬β¬β¬\nβ¬β¬β¬",
        "β¬β¬β¬\nβ¬πβ¬\nβ¬β¬β¬",
        "β¬β¬οΈβ¬\nβ¬πβ¬\nβ¬β¬β¬",
        "β¬β¬οΈβοΈ\nβ¬πβ¬\nβ¬β¬β¬",
        "β¬β¬οΈβοΈ\nβ¬πβ‘οΈ\nβ¬β¬β¬",
        "β¬β¬οΈβοΈ\nβ¬πβ‘οΈ\nβ¬β¬βοΈ",
        "β¬β¬οΈβοΈ\nβ¬πβ‘οΈ\nβ¬β¬οΈβοΈ",
        "β¬β¬οΈβοΈ\nβ¬πβ‘οΈ\nβοΈβ¬οΈβοΈ",
        "β¬β¬οΈβοΈ\nβ¬οΈπβ‘οΈ\nβοΈβ¬οΈβοΈ",
        "βοΈβ¬οΈβοΈ\nβ¬οΈπβ‘οΈ\nβοΈβ¬οΈβοΈ",
    ]
    event = await edit_or_reply(event, "fleaveme....")
    await asyncio.sleep(2)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])


@bot.on(admin_cmd(pattern=r"loveu$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"loveu$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(70)
    event = await edit_or_reply(event, "loveu")
    animation_chars = [
        "π",
        "π©βπ¨",
        "π",
        "π",
        "π€£",
        "π",
        "π",
        "π",
        "π",
        "βΊ",
        "π",
        "π€",
        "π€¨",
        "π",
        "π",
        "πΆ",
        "π£",
        "π₯",
        "π?",
        "π€",
        "π―",
        "π΄",
        "π",
        "π",
        "βΉ",
        "π",
        "π",
        "π",
        "π",
        "π’",
        "π­",
        "π€―",
        "π",
        "β€",
        "I Love Youβ€",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 35])


@bot.on(admin_cmd(pattern=r"plane$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"plane$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "Wait for plane...")
    await event.edit("β-------------")
    await event.edit("-β------------")
    await event.edit("--β-----------")
    await event.edit("---β----------")
    await event.edit("----β---------")
    await event.edit("-----β--------")
    await event.edit("------β-------")
    await event.edit("-------β------")
    await event.edit("--------β-----")
    await event.edit("---------β----")
    await event.edit("----------β---")
    await event.edit("-----------β--")
    await event.edit("------------β-")
    await event.edit("-------------β")
    await asyncio.sleep(3)


@bot.on(admin_cmd(pattern=r"police$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"police$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(12)
    event = await edit_or_reply(event, "Police")
    animation_chars = [
        "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
        "π΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄",
        "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
        "π΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄",
        "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
        "π΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄",
        "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
        "π΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄",
        "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
        "π΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄",
        "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])


@bot.on(admin_cmd(pattern=r"jio$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"jio$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(19)
    event = await edit_or_reply(event, "jio network boosting...")
    animation_chars = [
        "`Connecting To JIO NETWORK ....`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "*Optimising JIO NETWORK...*",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "**JIO NETWORK Boosted....**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 19])


@bot.on(admin_cmd(pattern=r"solarsystem$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"solarsystem$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(80)
    event = await edit_or_reply(event, "solarsystem")
    animation_chars = [
        "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
        "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
        "`βΌοΈπβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈββΌοΈ`",
        "`βΌοΈβΌοΈβΌοΈπβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈββΌοΈβΌοΈβΌοΈ`",
        "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
        "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
        "`βΌοΈββΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈπβΌοΈ`",
        "`βΌοΈβΌοΈβΌοΈββΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈπβΌοΈβΌοΈβΌοΈ`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


CMD_HELP.update(
    {
        "animation2": """**Plugin : **`animation2`
        
**Commands in animation2 are **
  β’  `.boxs`
  β’  `.rain`
  β’  `.deploy`
  β’  `.dump`
  β’  `.fleaveme`
  β’  `.loveu`
  β’  `.plane`
  β’  `.police`
  β’  `.jio`
  β’  `.solarsystem`
  
**Function : **__Different kinds of animation commands check yourself for their animation .__"""
    }
)
