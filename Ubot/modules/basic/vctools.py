# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import asyncio
from random import randint
from typing import Optional
from contextlib import suppress

from pyrogram import Client, enums, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message
from . import *
from ubotlibs.ubot.helper import get_arg
from ubotlibs.ubot.helper.basic import edit_or_reply

async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await client.invoke(GetFullChannel(channel=chat_peer))
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await message.edit(f"**No group call Found** {err_msg}")
    return False


@Client.on_message(filters.command(["joinos"], ".") & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command(["joinvc"], cmds) & filters.me)
async def joinvc(client: Client, message: Message):
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    if message.from_user.id != client.me.id:
        ky = await message.reply("Processing...")
    else:
        ky = await message.edit("Processing....")
    with suppress(ValueError):
        chat_id = int(chat_id)
    try:
        await client.group_call.start(chat_id)
        await ky.edit(f"**Berhasil Join Ke Obrolan Suara**\n└ **Chat ID**: {chat_id}")
        await asyncio.sleep(5)
        await client.group_call.set_is_mute(True)
        await asyncio.sleep(7200) 
    except asyncio.TimeoutError:
        await client.group_call.stop()
        return await ky.edit("**Waktu Habis ! Keluar dari obrolan suara**\n└ **Chat ID** : `{chat_id}`")
    except Exception as e:
        return await ky.edit(f"ERROR: {e}")
    finally:
        await client.group_call.stop()
    await ky.edit(f"**Waktu Habis..**\n**Berhasil Turun Dari Obrolan Suara**\n└ **Chat ID** : `{chat_id}`")


@Client.on_message(filters.command(["leaveos"], ".") & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command(["leavevc"], cmds) & filters.me)
async def leavevc(client: Client, message: Message):
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    if message.from_user.id != client.me.id:
        ky = await message.reply("`Processing...`")
    else:
        ky = await message.edit("`Processing....`")
    with suppress(ValueError):
        chat_id = int(chat_id)
    try:
        await client.group_call.stop()
    except Exception as e:
        return await edit_or_reply(message, f"**ERROR:** `{e}`")
    msg = "**Berhasil Meninggalkan Obrolan Suara**\n**"
    if chat_id:
        msg += f"\n└ **Chat ID:** `{chat_id}`"
    await ky.edit(msg)


@Client.on_message(filters.command(["startvcs"], ".") & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command(["startvc"], cmds) & filters.me)
async def opengc(client: Client, message: Message):
    flags = " ".join(message.command[1:])
    ky = await edit_or_reply(message, "`Processing . . .`")
    vctitle = get_arg(message)
    if flags == enums.ChatType.CHANNEL:
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    args = f"**Obrolan Suara Aktif**\n • **Chat ID** : `{chat_id}`"
    try:
        if not vctitle:
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                )
            )
        else:
            args += f"\n • **Title:** `{vctitle}`"
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                    title=vctitle,
                )
            )
        await ky.edit(args)
    except Exception as e:
        await ky.edit(f"**INFO:** `{e}`")


@Client.on_message(filters.command(["stopvcs"], ".") & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command(["stopvc"], cmds) & filters.me)
async def end_vc_(client: Client, message: Message):
    """Processing..."""
    chat_id = message.chat.id
    if not (
        group_call := (await get_group_call(client, message, err_msg=", Kesalahan..."))
    ):
        return
    await client.send(DiscardGroupCall(call=group_call))
    await edit_or_reply(
        message, f"**Obrolan Suara Diakhiri**\n • **Chat ID** : `{chat_id}`"
    )


add_command_help(
    "voicechat",
    [
        [f"startvc", "Start voice chat group."],
        [f"stopvc", "End voice chat group."],
        [f"joinvc", "Join voice chat group."],
        [f"leavevc", "Leave voice chat group."],
    ],
)
