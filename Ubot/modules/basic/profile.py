# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

import os
from asyncio import sleep
import os
from . import *

from ubotlibs.ubot.helper.PyroHelpers import ReplyCheck
from pyrogram import Client, filters
from pyrogram.types import Message



flood = {}
profile_photo = "https://telegra.ph//file/94cc3c815a9e063dad4f0.jpg"

async def list_admins(client: Client, chat_id: int):
    global admins_in_chat
    if chat_id in admins_in_chat:
        interval = time() - admins_in_chat[chat_id]["last_updated_at"]
        if interval < 3600:
            return admins_in_chat[chat_id]["data"]

    admins_in_chat[chat_id] = {
        "last_updated_at": time(),
        "data": [
            member.user.id
            async for member in client.get_chat_members(
                chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS
            )
        ],
    }
    return admins_in_chat[chat_id]["data"]


async def extract_userid(message, text: str):
    def is_int(text: str):
        try:
            int(text)
        except ValueError:
            return False
        return True

    text = text.strip()

    if is_int(text):
        return int(text)

    entities = message.entities
    app = message._client
    if len(entities) < 2:
        return (await app.get_users(text)).id
    entity = entities[1]
    if entity.type == "mention":
        return (await app.get_users(text)).id
    if entity.type == "text_mention":
        return entity.user.id
    return None


async def extract_user_and_reason(message, sender_chat=False):
    args = message.text.strip().split()
    text = message.text
    user = None
    reason = None
    if message.reply_to_message:
        reply = message.reply_to_message
        if not reply.from_user:
            if (
                reply.sender_chat
                and reply.sender_chat != message.chat.id
                and sender_chat
            ):
                id_ = reply.sender_chat.id
            else:
                return None, None
        else:
            id_ = reply.from_user.id

        if len(args) < 2:
            reason = None
        else:
            reason = text.split(None, 1)[1]
        return id_, reason

    if len(args) == 2:
        user = text.split(None, 1)[1]
        return await extract_userid(message, user), None

    if len(args) > 2:
        user, reason = text.split(None, 2)[1:]
        return await extract_userid(message, user), reason

    return user, reason
    
async def extract_user(message):
    return (await extract_user_and_reason(message))[0]

@Ubot(["unblock"], cmds)
async def unblock_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    tex = await message.reply_text("`Processing . . .`")
    if not user_id:
        return await message.edit(
            "Berikan username atau reply pesan untuk membuka blokir."
        )
    if user_id == client.me.id:
        return await tex.edit("Ok done ✅.")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await message.edit(f"**Berhasil membuka blokir** {umention}")


@Ubot(["block"], cmds)
async def block_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    tex = await message.reply_text("`Processing . . .`")
    if not user_id:
        return await tex.edit_text(
            "Berikan username untuk di blok."
        )
    if user_id == client.me.id:
        return await tex.edit_text("ok ✅.")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit_text(f"**Berhasil mem-blokir** {umention}")


@Ubot(["setname"], cmds)
async def setname(client: Client, message: Message):
    tex = await message.reply_text("`Processing . . .`")
    if len(message.command) == 1:
        return await tex.edit(
            "Berikan text untuk diatur sebagai nama anda."
        )
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await tex.edit(f"**Berhasil mengganti nama menjadi** `{name}`")
        except Exception as e:
            await tex.edit(f"**ERROR:** `{e}`")
    else:
        return await tex.edit(
            "Berikan text untuk diatur sebagai nama anda."
        )


@Ubot(["setbio"], cmds)
async def set_bio(client: Client, message: Message):
    tex = await message.edit_text("`Processing . . .`")
    if len(message.command) == 1:
        return await tex.edit("Berikan text untuk diatur sebagai bio.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await tex.edit(f"**Berhasil mengganti bio menjadi** `{bio}`")
        except Exception as e:
            await tex.edit(f"**ERROR:** `{e}`")
    else:
        return await tex.edit("Berikan text untuk diatur sebagai bio.")

@Ubot(["setpp"], cmds)
async def set_pfp(client: Client, message: Message):
    replied = message.reply_to_message
    if (
        replied
        and replied.media
        and (
            replied.photo
            or (replied.document and "image" in replied.document.mime_type)
        )
    ):
        profile_photo = profile_photo
        await client.download_media(message=replied, file_name=profile_photo)
        await client.set_profile_photo(profile_photo)
        if os.path.exists(profile_photo):
            os.remove(profile_photo)
        await message.reply_text("**Foto profil berhasil di ganti.**")
    else:
        await message.reply_text(
            "Balas ke gamabr/foto untuk atur sebagai foto profil"
        )
        await sleep(3)
        await message.delete()




add_command_help(
    "profile",
    [
        [f"block", "Blokir pengguna"],
        [f"unblock", "membuka blokir"],
        [f"setname", "mengatur nama anda."],
        [f"setbio", "mengatur bio anda."],
        
    ],
)
