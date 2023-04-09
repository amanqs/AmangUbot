# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

import asyncio
from pyrogram import Client
from pyrogram.errors import YouBlockedUser
from pyrogram.types import Message
from . import *
from ubotlibs.ubot.utils import extract_user

@Ubot(["sg"], "")
async def sg(client: Client, message: Message):
    args = await extract_user(message)
    lol = await message.edit("<code>Processing...</code>")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            return await lol.edit("<code>Please specify a valid user!</code>")
    sg = "esgebotol"
    try:
         await client.join_chat(sg)
         await asyncio.sleep(0.5)
         await client.send_message(sg, f"@Sangmata_beta_bot Allhistory {user.id}")
    except:
         return
    await asyncio.sleep(1)
    async for stalk in client.search_messages(sg, limit=1):
        if not stalk:
            await message.edit("<code>Orang Ini Belum Pernah Mengganti Namanya</code>")
            return
        elif stalk:
            await message.edit(stalk.text)
            await client.leave_chat(-1001936325181)


add_command_help(
    "sangmata",
    [
        [f"sg [reply/userid/username]",
            "mengambil info history pengguna.",
        ],
    ],
)
