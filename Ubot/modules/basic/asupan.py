# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import asyncio
from asyncio import gather
from random import choice
from pyrogram import Client, filters, enums
from pyrogram.types import ChatPermissions, ChatPrivileges, Message
from ubotlibs.ubot.helper import edit_or_reply, ReplyCheck
from . import *
from ubotlibs.ubot.database.accesdb import *
from config import *


@Ubot(["asupan"], cmds)
async def asupan(client: Client, message: Message):
    if message.chat.id in BL_UBOT:
        return await message.reply("**Tidak bisa di gunakan di Group Support**")
    ky = await message.edit("`Mencari asupan... 🔎`")
    await gather(
        ky.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "punyakenkan", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )

# WARNING PORNO VIDEO THIS !!!

@Ubot(["Bokep"], cmds)
async def asupin(client: Client, message: Message):
    if message.chat.id in BL_UBOT:
        return await message.reply("**Tidak bisa di gunakan di Group Support**")
    ran = await message.edit("`Mencari bahan... 🔎`")
    await gather(
        ran.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "bahaninimah", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot(["Ayang"], cmds)
async def ay(client, message):
    if message.chat.id in BL_UBOT:
        return await message.reply("**Tidak bisa di gunakan di Group Support**")
    rizky = await message.edit("🔎 `Search Ayang...`")
    await message.reply_photo(
        choice(
            [
                rz.photo.file_id
                async for rz in client.search_messages(
                    "CeweLogoPack", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Upload by {client.me.mention}",
    )

    await rizky.delete()


@Ubot(["ppcp"], cmds)
async def pcp(client, message):
    if message.chat.id in BL_UBOT:
        return await message.reply("**Tidak bisa di gunakan di Group Support**")
    darmi = await message.edit("🔎 `Search PPCP...`")
    await message.reply_photo(
        choice(
            [
                ky.photo.file_id
                async for ky in client.search_messages(
                    "ppcpcilik", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Upload by {client.me.mention}",
    )

    await darmi.delete()
    
    
@Ubot(["ppcp2"], cmds)
async def cp(client, message):
    if message.chat.id in BL_UBOT:
        return await message.reply("**Tidak bisa di gunakan di Group Support**")
    dar = await message.edit("🔎 `Search Ppcp 2...`")
    await message.reply_photo(
        choice(
            [
                cot.photo.file_id
                async for cot in client.search_messages(
                    "mentahanppcp", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Upload by {client.me.mention}",
    )

    await dar.delete()
    
    
@Ubot(["anime"], cmds)
async def anim(client, message):
    if message.chat.id in BL_UBOT:
        return await message.reply("**Tidak bisa di gunakan di Group Support**")
    iis = await message.edit("🔎 `Search Anime...`")
    await message.reply_photo(
        choice(
            [
                jir.photo.file_id
                async for jir in client.search_messages(
                    "animehikarixa", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Upload by {client.me.mention}",
    )

    await iis.delete()
    
   
@Ubot(["anime2"], cmds)
async def nimek(client, message):
    if message.chat.id in BL_UBOT:
        return await message.reply("**Tidak bisa di gunakan di Group Support**")
    erna = await message.edit("🔎 `Search Anime...`")
    await message.reply_photo(
        choice(
            [
                tai.photo.file_id
                async for tai in client.search_messages(
                    "Anime_WallpapersHD", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Upload by {client.me.mention}",
    )

    await erna.delete()
    
    
@Ubot(["bugil"], cmds)
async def sange(client, message):
    if message.chat.id in BL_GCAST:
        return await message.reply("**Tidak bisa di gunakan di Group Support**")
    kntl = await message.edit("🔎 `Search PP Bugil...`")
    await message.reply_photo(
        choice(
            [
                pler.photo.file_id
                async for pler in client.search_messages(
                    "durovbgst", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Upload by {client.me.mention}",
    )

    await kntl.delete()
    
@Ubot(["pap"], cmds)
async def bugil(client, message):
    if message.chat.id in BL_UBOT:
        return await message.reply("**Tidak bisa di gunakan di Group Support**")
    kazu = await message.edit("🔎 `Nih PAP Nya...`")
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "mm_kyran", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption="**Buat Kamu..**",
    )

    await kazu.delete()


add_command_help(
    "asupan",[
        [f"pap", "Random PAP",],
        [f"asupan", "Asupan video TikTok",],
        [f"ayang", "Mencari Foto ayang kamu /nNote: Modul ini buat cwo yang jomblo."],
        [f"ppcp", "Mencari Foto PP Couple Random."],
        [f"ppcp2", "Mencari Foto PP Couple Random 2."],
        [f"bokep", "to send random porno videos."],
        [f"bugil", "to send photo porno random."],
        [f"anime", "Mencari Foto PP Couple Anime."],
        [f"anime2", "Mencari Foto Anime."],
    ],
)
