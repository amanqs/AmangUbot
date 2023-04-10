# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from . import *


@Ubot(["dm"], cmds)
async def dm(c: Client, m: Message):
    await m.edit("` Proccessing.....`")
    quantity = 1
    inp = m.text.split(None, 2)[1]
    user = await c.get_chat(inp)
    spam_text = ' '.join(m.command[2:])
    quantity = int(quantity)

    if m.reply_to_message:
        reply_to_id = m.reply_to_message.message_id
        for _ in range(quantity):
            await m.edit("Message Sended Successfully !")
            await c.send_message(user.id, spam_text,
                                      reply_to_messsge_id=reply_to_id)
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await c.send_message(user.id, spam_text)
        await m.edit("Message Sended Successfully !")
        await asyncio.sleep(0.15)


add_command_help(
    "pm",
    [
        [f"dm @username kata", "Untuk Mengirim Pesan Tanpa Harus Kedalam Roomchat.",],
    ],
)
