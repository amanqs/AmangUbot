# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

from pyrogram import Client, filters
from pyrogram.types import Message
from . import *
from ubotlibs.ubot.helper import edit_or_reply



@Ubot(["buat"], cmds)
async def create(client: Client, message: Message):
    if len(message.command) < 3:
        return await message.reply(f"**buat gc => Untuk Membuat Grup, buat ch => Untuk Mebuat Channel**"
        )
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    xd = await message.edit("`Processing...`")
    desc = "Welcome To My " + ("Group" if group_type == "gc" else "Channel")
    if group_type == "gc":  # for supergroup
        _id = await client.create_supergroup(group_name, desc)
        link = await client.get_chat(_id.id)
        await xd.edit(
            f"**Successfully Created Telegram Group: [{group_name}]({link.invite_link})**",
            disable_web_page_preview=True,
        )
    elif group_type == "ch":  # for channel
        _id = await client.create_channel(group_name, desc)
        link = await client.get_chat(_id.id)
        await xd.edit(
            f"**Successfully Created Telegram Channel: [{group_name}]({link.invite_link})**",
            disable_web_page_preview=True,
        )




add_command_help(
    "buat",
    [
        [f"buat gc atau ch", "Membuat Channel atau Group"],
    ],
)
