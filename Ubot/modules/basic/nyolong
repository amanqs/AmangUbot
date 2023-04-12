# Credits Thx Tomi Setiawan
# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

from . import *
from ubotlibs.ubot.utils import get_arg



@Client.on_message(filters.command(["curi"], cmds) & filters.me)
async def copy_msg(client: Client, message: Message):
    Tm = await message.reply("`Processing...`")
    link = get_arg(message)
    if not link:
        return await Tm.edit(f"<b><code>{message.text}</code> [link_konten_telegram]</b>")
    if link.startswith(("https", "t.me")):
        msg_id = int(link.split("/")[-1])
        if "t.me/c/" in link:
            chat = int("-100" + str(link.split("/")[-2]))
        else:
            chat = str(link.split("/")[-2])
        try:
            get = await client.get_messages(chat, msg_id)
            await get.copy(message.chat.id)
            return await Tm.delete()
        except Exception as error:
            await Tm.edit(error)
    else:
        await Tm.edit("`Berikan link yang valid.`")



add_command_help(
    "nyolong",
    [
        [f"curi", "nyolong konten orang"],
    ],
)
