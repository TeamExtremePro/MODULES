# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot plugin_info command """

from . import CmdHelp
from userbot.utils import admin_cmd

@borg.on(admin_cmd(outgoing=True, pattern="plinfo(?: |$)(.*)"))
async def info(event):
    """ For .plinfo command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CmdHelp:
            await event.edit(str(CmdHelp[args]))
        else:
            await event.edit("Please specify a valid plugin name.")
    else:
        await event.edit("Please specify which plugin do you want help for !!\
            \nUsage: .pinfo <plugin name>")
        string = ""
        for i in CmdHelp:
            string += "`" + str(i)
            string += "`\n"
        await event.reply(string)
