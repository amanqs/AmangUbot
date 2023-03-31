
import asyncio

from pyrogram import Client, enums, filters
from pyrogram.types import Message
from . import *
from Ubot.core.db import *
from ubotlibs.ubot.utils.tools import get_arg



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

@Ubot("setlog", "")
async def set_log(client, message):
    try:
        botlog_chat_id = int(message.text.split(" ")[1])
    except (ValueError, IndexError):
        await message.reply_text("**Format yang Anda masukkan salah. Gunakan format** `setlog id_grup`.")
        return
    user_id = client.me.id
    chat_id = message.chat.id
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
