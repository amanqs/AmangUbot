# Copyright (C) 2020-2021 by Toni880@Github, < https://github.com/Toni880 >.
#
# This file is part of < https://github.com/Toni880/Prime-Userbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Toni880/Prime-Userbot/blob/master/LICENSE >
# kenkan
# abdul
#
# All rights reserved.


import os

from pyrogram import *
from pyrogram import Client, filters
from pyrogram.errors import RPCError
from pyrogram.types import *

from ubotlibs.ubot.utils import get_arg
from . import *

@Client.on_message(filters.command("copy", cmds) & filters.me)
async def nyolongnih(client, message):
    await message.edit("Procesing...")
    link = get_arg(message)
    msg_id = int(link.split("/")[-1])
    if "t.me/c/" in link:
        try:
            chat = int("-100" + str(link.split("/")[-2]))
            dia = await client.get_messages(chat, msg_id)
        except RPCError:
            await message.edit("Looks like an error occurred")
    else:
        try:
            chat = str(link.split("/")[-2])
            dia = await client.get_messages(chat, msg_id)
        except RPCError:
            await message.edit("Looks like an error occurred")
    anjing = dia.caption or None
    if dia.text:
        await dia.copy(message.chat.id)
        await message.delete()
    if dia.photo:
        anu = await client.download_media(dia)
        await client.send_photo(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.video:
        anu = await client.download_media(dia)
        await client.send_video(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.audio:
        anu = await client.download_media(dia)
        await client.send_audio(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.voice:
        anu = await client.download_media(dia)
        await client.send_voice(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.document:
        anu = await client.download_media(dia)
        await client.send_document(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)
    else:
        await message.edit("Looks like an error occurred")


@Client.on_message(filters.command("getmsg", cmds) & filters.me)
async def pencuri(client, message):
    dia = message.reply_to_message
    if not dia:
        await message.edit("Please reply to the media")
    anjing = dia.caption or None
    await message.edit("Procesing...")
    if dia.text:
        await dia.copy(message.chat.id)
        await message.delete()
    if dia.photo:
        anu = await client.download_media(dia)
        await client.send_photo(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.video:
        anu = await client.download_media(dia)
        await client.send_video(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.audio:
        anu = await client.download_media(dia)
        await client.send_audio(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.voice:
        anu = await client.download_media(dia)
        await client.send_voice(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.document:
        anu = await client.download_media(dia)
        await client.send_document(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)
    else:
        await message.edit("Looks like an error occurred")


@Client.on_message(filters.command("apani", cmds) & filters.me)
async def ambil(client: Client, message: Message):
    dia = message.reply_to_message
    if not dia:
        await message.edit("Looks like an error occurred")
    dia.caption or None
    if dia.photo:
        anu = await client.download_media(dia)
        await client.send_photo(message.from_user.id, anu)
        await message.delete()
        os.remove(anu)

    if dia.video:
        anu = await client.download_media(dia)
        await client.send_video(message.from_user.id, anu)
        await message.delete()
        os.remove(anu)

    if dia.audio:
        anu = await client.download_media(dia)
        await client.send_audio(message.from_user.id, anu)
        await message.delete()
        os.remove(anu)

    if dia.voice:
        anu = await client.download_media(dia)
        await client.send_voice(message.from_user.id, anu)
        await message.delete()
        os.remove(anu)


add_command_help(
    "cpymsg",
    [
        [
            "copy <link protected channel.>",
            "Clone restricted media."],
        [   "getmsg <reply message>",
            "Clone from the protected media or timer message."],
        [   "apani <reply message>",
            "take timer message on PM."],
    ],
)
