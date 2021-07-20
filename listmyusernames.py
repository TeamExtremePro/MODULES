# For @UniBorg
# (c) Shrimadhav U K

from userbotserbotserbotelethon import events, functions, types
from userbotserbotserbotniborg.util import admin_cmd
from userbotserbotserbot import CMD_HELP
from userbotserbotserbotelethon.tl.functions.channels import GetAdminedPublicChannelsRequest

@borg.on(admin_cmd("listmyusernames"))

async def mine(event):
    """ For .reserved command, get a list of your reserved usernames. """
    result = await bot(GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"{channel_obj.title}\n@{channel_obj.username}\n\n"
    await event.edit(output_str)



CMD_HELP.update(
    {
        "LIST MY USERNAMES": "**Plugin : **`listmyusernames`\
    \n\n**Syntax : **`.listmyusernames`\
    \n**Function : **this plugin give you your all channel and groups usernamen"
    }
)
