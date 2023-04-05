from asyncio import sleep
from pyrogram import Client, filters
from Ubot.core.db import *
from pyrogram.types import Message
from ubotlibs.ubot.utils.tools import *
from . import *


@Ubot("save", "")
async def simpan_note(client, message):
    name = get_arg(message)
    user_id = message.from_user.id
    chat_id = message.chat.id
    msg = message.reply_to_message
    if not msg:
        return await message.reply("`Silakan balas ke pesan.`")
    botlog_chat_id = await get_botlog(user_id)
    if not botlog_chat_id:
        return await message.reply("`Maaf, tidak dapat menemukan ID chat log bot.`\nPastikan Anda Telah Mengtur Log Group Anda")
    anu = await msg.forward(botlog_chat_id)
    msg_id = anu.id
    await client.send_message(botlog_chat_id,
        f"#NOTE\nKEYWORD: {name}"
        "\n\nPesan berikut disimpan sebagai data balasan catatan untuk obrolan, mohon jangan dihapus !!",
    )
    await sleep(1)
    await save_note(user_id, name, msg_id)
    await message.reply(f"**Berhasil menyimpan catatan dengan nama** `{name}`")



@Ubot("get", "")
async def panggil_notes(client, message):
    name = get_arg(message)
    user_id = message.from_user.id
    botlog_chat_id = await get_botlog(user_id)
    _note = await get_note(user_id, name)
    if not _note:
        return await message.reply("`Tidak ada catatan seperti itu.`")
    msg_o = await client.get_messages(botlog_chat_id, _note)
    await msg_o.copy(message.chat.id, reply_to_message_id=message.id)


@Ubot("rm", "")
async def remove_notes(client, message):
    name = get_arg(message)
    user_id = message.from_user.id
    deleted = await delete_note(user_id, name)
    if deleted:
        await message.reply("**Berhasil Menghapus Catatan:** `{}`".format(name))
    else:
        await message.reply("**Tidak dapat menemukan catatan:** `{}`".format(name))


@Ubot("notes", "")
async def get_notes(client, message):
    user_id = message.from_user.id
    botlog_chat_id = await get_botlog(user_id)
    _notes = await get_note_names(user_id)
    if not _notes:
        return await message.reply("**Tidak ada catatan.**")
    msg = f"**➣ Daftar catatan**\n\n"
    for note in _notes:
        msg += f"**•** `{note}`\n"
    await message.reply(msg)


add_command_help(
    "notes",
    [
        [f" save [text/reply]",
            "Simpan pesan ke Group. (bisa menggunakan stiker)"],
        [f" get [nama]",
            "Ambil catatan ke tersimpan"],
        [f" notes",
            "Lihat Daftar Catatan"],
        [f" rm [nama]",
            "Menghapus nama catatan"],
    ],
)
