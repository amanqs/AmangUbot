# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

import re
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton as Ikb
from . import *
from Ubot.core.db  import *
from Ubot.core.filter import *

@Ubot("adfil", cmds)
async def save_filters(client, message):
    if len(message.command) < 2 or not message.reply_to_message:
        return await message.reply_text(
            f"**Gunakan Format:**\nbalas kepesan atau sticker `savefilter` [nama filter] untuk save filter."
        )
    if (
        not message.reply_to_message.text
        and not message.reply_to_message.sticker
    ):
        return await message.reply_text(
            "**Hanya bisa save text atau sticker.**"
        )
    name = message.text.split(None, 1)[1].strip()
    if not name:
        return await message.reply_text(
            f"**Gunakan Format:**\n`filter` [nama filter]"
        )
    chat_id = message.chat.id
    user_id = client.me.id
    if message.chat.id in BL_GCAST:
        await message.edit("Filter tidak diperkenankan di group support")
        return
    _type = "text" if message.reply_to_message.text else "sticker"
    _filter = {
        "type": _type,
        "data": message.reply_to_message.text.markdown
        if _type == "text"
        else message.reply_to_message.sticker.file_id,
    }
    await save_filter(user_id, chat_id, name, _filter)
    await message.reply_text(f"**Filter {name} disimpan!.**")

@Ubot("filters", cmds)
async def get_filterss(client, message):
    user_id = client.me.id
    chat_id = message.chat.id
    _filters = await get_filters_names(user_id, chat_id)
    if not _filters:
        return await message.reply_text("**Tidak ada filter tersimpan di group ini.**")
    _filters.sort()
    msg = f"Daftar filter tersimpan di {message.chat.title}\n"
    for _filter in _filters:
        msg += f"**-** `{_filter}`\n"
    await message.reply_text(msg)

@Ubot("stfil", cmds)
async def del_filter(client, message):
    if len(message.command) < 2:
        return await message.reply_text(f"**Gunakan Format:**\n`stopfilter` [nama filter]")
    user_id = client.me.id
    chat_id = message.chat.id
    name = message.text.split(None, 1)[1].strip()
    if not name:
        return await message.reply_text(f"**Gunakan format:**\n`stopfilter` [nama filter]")
    
    deleted = await delete_filter(user_id, chat_id, name)
    if deleted:
        await message.reply_text(f"*Filter {name} berhasil dihapus.**")
    else:
        await message.reply_text("**Filter tidak ditemukan.**")

@Client.on_message(filters.text & ~filters.private & ~filters.via_bot & ~filters.forwarded,group=chat_filters_group)
async def filters_re(client, message):
    text = message.text.lower().strip()
    if not text:
        return
    user_id = client.me.id
    chat_id = message.chat.id
    list_of_filters = await get_filters_names(user_id, chat_id)
    for word in list_of_filters:
        pattern = r"( |^|[^\w])" + re.escape(word) + r"( |$|[^\w])"
        if re.search(pattern, text, flags=re.IGNORECASE):
            _filter = await get_filter(user_id, chat_id, word)
            data_type = _filter["type"]
            data = _filter["data"]
            if data_type == "text":
                keyb = None
                if re.findall(r"\[.+\,.+\]", data):
                    keyboard = extract_text_and_keyb(ikb, data)
                    if keyboard:
                        data, keyb = keyboard

                if message.reply_to_message:
                    await message.reply_to_message.reply_text(
                        data,
                        reply_markup=keyb,
                        disable_web_page_preview=True,
                    )

                    if text.startswith("~"):
                        await message.delete()
                    return

                return await message.reply_text(
                    data,
                    reply_markup=keyb,
                    disable_web_page_preview=True,
                )
            if message.reply_to_message:
                await message.reply_to_message.reply_sticker(data)

                if text.startswith("~"):
                    await message.delete()
                return
            return await message.reply_sticker(data)
        
add_command_help(
    "filter",
    [
        [f"adfil <balas ke pesan atau sticker> <triger/nama filer>", "Save filters."],
        [f"stfil <triger/nama filter>", "Menghapus filter."],
        [f"filters", "Melihat list filter."],
    ],
)