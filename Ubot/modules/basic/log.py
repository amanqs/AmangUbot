# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import asyncio

from pyrogram import Client, enums, filters
from pyrogram.types import Message
from . import *
from Ubot.core.db import *
from ubotlibs.ubot.utils.tools import get_arg


"""
@Client.on_message(
    filters.private
    & filters.incoming
    & ~filters.service
    & ~filters.me
    & ~filters.bot
    & ~filters.via_bot
)
async def pm_log(client, message):
    user_id = client.me.id
    botlog_chat_id = await get_log_groups(user_id)
    user = message.from_user.id
    biji = message.from_user.first_name
    sempak = message.text
    await client.send_message(
                botlog_chat_id,
                f"💌 <b><u>MENERUSKAN PESAN BARU</u></b>\n<b> • Dari :</b> {biji}\n<b> • User ID :</b> <code>{user}</code>\n<b> • PESAN :</b> <code>{sempak}</code>\n ",
                parse_mode=enums.ParseMode.HTML,
            )
  
@Client.on_message(filters.group & filters.mentioned & filters.incoming & ~filters.bot & ~filters.via_bot)
async def log_tagged_messages(client, message):
    chat_id = message.chat.id
    user_id = client.me.id
    botlog_chat_id = await get_botlog(user_id)
    knl = f"📨<b><u>ANDA TELAH DI TAG</u></b>\n<b> • Dari : </b>{message.from_user.mention}"
    knl += f"\n<b> • Grup : </b>{message.chat.title}"
    knl += f"\n<b> • 👀 </b><a href = '{message.link}'>Lihat Pesan</a>"
    knl += f"\n<b> • Message : </b><code>{message.text}</code>"
    await asyncio.sleep(0.5)
    await client.send_message(
        botlog_chat_id,
        knl,
        parse_mode=enums.ParseMode.HTML,
        disable_web_page_preview=True,
    )
"""


@Ubot("setlog", cmds)
async def set_log(client, message):
    botlog_chat_id = message.chat.id
    user_id = client.me.id
    chat = await client.get_chat(botlog_chat_id)
    if chat.type == "private":
        return await message.reply("Maaf, perintah ini hanya berlaku untuk grup.")
    await set_botlog(user_id, botlog_chat_id)
    await message.reply_text(f"**ID Grup Log telah diatur ke `{botlog_chat_id}` untuk grup ini.**")

add_command_help(
    "logger",
    [
        [
            "setlog",
            "Sebelum mengaktifkan fitur pmlog dan taglog anda harus mengatur setlog id_grup log anda terlebih dahulu.",
        ],
    ],
)
