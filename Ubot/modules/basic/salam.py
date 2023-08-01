"""
Credit:
Code By:
- Kynan (https://github.com/naya1504)
- Amang (https://github.com/amanqs)
"""


import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from . import *
from ubotlibs.ubot.helper.basic import edit_or_reply
from ubotlibs.ubot.helper.PyroHelpers import ReplyCheck


@Ubot("p", "")
async def salamone(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Assalamualaikum...",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot("pe", "")
async def salamdua(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Assalamualaikum Warahmatullahi Wabarakatuh",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot("l", "")
async def jwbsalam(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Wa'alaikumsalam...",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot("el", "")
async def jwbsalamlngkp(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Wa'alaikumsalam Warahmatullahi Wabarakatuh",
            reply_to_message_id=ReplyCheck(message),
        ),
    )



@Ubot("as", "")
async def salamarab(client: Client, message: Message):
    xx = await edit_or_reply(message, "Salam Dulu Gua..")
    await asyncio.sleep(2)
    await xx.edit("السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")

add_command_help(
    "salam",
    [
        [f"p", "Assalamualaikum."],
        [f"pe", "Assalamualaikum Warahmatullahi Wabarakatuh."],
        [f"l", "Wa'alaikumsalam."],
        [f"as", "Assalamualaikum Bahas arab."],
    ]
)