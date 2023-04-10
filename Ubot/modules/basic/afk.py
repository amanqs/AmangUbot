# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

from datetime import datetime
from pyrogram import filters, Client
from pyrogram.types import Message
from Ubot.core.db import *
from ubotlibs.ubot.utils import get_text
from . import *


afk_sanity_check: dict = {}
afkstr = """
#AFK Aktif\n Alasan {}
"""
onlinestr ="""
#AFK Tidak Aktif\nAlasan {}
"""
async def is_afk_(f, client, message):
    user_id = client.me.id
    af_k_c = await check_afk(user_id)
    if af_k_c:
        return bool(True)
    else:
        return bool(False)
    
is_afk = filters.create(func=is_afk_, name="is_afk_")

@Ubot("afk", cmds)
async def set_afk(client, message):
    if len(message.command) == 1:
        return await message.reply(f"**Gunakan format dengan berikan alasan**\n\n**Contoh** : `afk berak`")
    user_id = client.me.id
    botlog = await get_log_groups(user_id)
    pablo = await message.edit("Processing..")
    msge = None
    msge = get_text(message)
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    if msge:
        msg = f"**❏ Sedang AFK**.\n** ╰ Alasan** : `{msge}`"
        await client.send_message(botlog, afkstr.format(msge))
        await go_afk(user_id, afk_start, msge)
    else:
        msg = "**❏ Sedang AFK**."
        await client.send_message(botlog, afkstr.format(msge))
        await go_afk(user_id, afk_start)
    await pablo.edit(msg)

@Client.on_message(
    is_afk
    & (filters.mentioned | filters.private)
    & ~filters.me
    & ~filters.bot
    & filters.incoming
)
async def afk_er(client, message):
    user_id = client.me.id
    if not message:
        return
    if not message.from_user:
        return
    if message.from_user.id == user_id:
        return
    use_r = int(user_id)
    if use_r not in afk_sanity_check.keys():
        afk_sanity_check[use_r] = 1
    else:
        afk_sanity_check[use_r] += 1
    if afk_sanity_check[use_r] == 5:
        await message.reply_text(
            "**❏ Sedang AFK**."
        )
        afk_sanity_check[use_r] += 1
        return
    if afk_sanity_check[use_r] > 5:
        return
    lol = await check_afk(user_id)
    reason = lol["reason"]
    if reason == "":
        reason = None
    back_alivee = datetime.now()
    afk_start = lol["time"]
    afk_end = back_alivee.replace(microsecond=0)
    total_afk_time = str((afk_end - afk_start))
    message_to_reply = (
        f"**❏ Sedang AFK**\n** ├ Waktu** :`{total_afk_time}`\n** ╰ Alasan** : `{reason}`"
        if reason
        else f"**❏ Sedang AFK**\n** ╰ Waktu** :`{total_afk_time}`"
    )
    await message.reply(message_to_reply)
    

@Client.on_message(filters.outgoing & filters.me & is_afk)
async def no_afke(client, message):
    user_id = client.me.id
    botlog = await get_log_groups(user_id)
    lol = await check_afk(user_id)
    back_alivee = datetime.now()
    afk_start = lol["time"]
    afk_end = back_alivee.replace(microsecond=0)
    total_afk_time = str((afk_end - afk_start))
    kk = await message.reply(f"**❏ Saya Kembali.**\n** ╰ AFK Selama** : {total_afk_time}")
    await kk.delete()
    await no_afk(user_id)
    await client.send_message(botlog, onlinestr.format(total_afk_time))

add_command_help(
    "afk",
    [
        [f"afk","Mengaktifkan mode afk.",
        ],
    ],
)