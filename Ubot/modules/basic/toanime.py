# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT
# Credits : TomiX


import os
import asyncio
import time
from pyrogram import Client, filters, enums
from pyrogram.types import *
from pyrogram.raw.functions.messages import DeleteHistory
from . import *



@Client.on_message(filters.command(["toanime"], cmds) & filters.me)
async def convert_image(client, message):
    if not message.reply_to_message:
        return await message.edit("**Mohon Balas Ke Foto**")
    bot = "qq_neural_anime_bot"
    if message.reply_to_message:
        cot = await message.edit("**Processing...**")
        await client.unblock_user(bot)
        ba = await message.reply_to_message.forward(bot)
        await asyncio.sleep(30)
        await ba.delete()
        await cot.delete()
        get_photo = []
        async for Toanime in client.search_messages(
            bot, filter=enums.MessagesFilter.PHOTO
        ):
            get_photo.append(InputMediaPhoto(Toanime.photo.file_id))
        await client.send_media_group(
            message.chat.id,
            media=get_photo,
            reply_to_message_id=message.id,
        )
        user_info = await client.resolve_peer(bot)
        return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))



@Client.on_message(filters.command(["togif"], cmds) & filters.me)
async def togif(client: Client, message: Message):
    TM = await message.reply("<b>Memproses...</b>")
    if not message.reply_to_message:
        return await TM.edit("<b>Balas ke Stiker...</b>")
    await TM.edit("<b>Downloading Sticker. . .</b>")
    file = await client.download_media(
        message.reply_to_message,
        f"Gift_Tomi_{message.from_user.id}.mp4",
    )
    try:
        await client.send_animation(
            message.chat.id, file, reply_to_message_id=message.id
        )
        os.remove(file)
        await TM.delete()
    except Exception as error:
        await TM.edit(error)