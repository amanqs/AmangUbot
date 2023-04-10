# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import asyncio
import io
import random
import textwrap
from pyrogram import Client, filters, enums
from pyrogram.types import Message
from pyrogram.errors import YouBlockedUser
from emoji import get_emoji_regexp
from PIL import Image, ImageDraw, ImageFont
from ubotlibs.ubot.helper.utility import get_arg
from . import *
from ubotlibs.ubot.helper.PyroHelpers import ReplyCheck


def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return get_emoji_regexp().sub("", inputString)

@Ubot(["q", "quotly"], cmds)
async def quotly(client: Client, message: Message):
    args = get_arg(message)
    if not message.reply_to_message and not args:
        return await message.edit("**Please Reply to Message**")
    bot = "QuotLyBot"
    if message.reply_to_message:
        await message.edit("`Making a Quote . . .`")
        await client.unblock_user(bot)
        if args:
            await client.send_message(bot, f"/qcolor {args}")
            await asyncio.sleep(1)
        else:
            pass
        await message.reply_to_message.forward(bot)
        await asyncio.sleep(5)
        async for quotly in client.search_messages(bot, limit=1):
            if quotly:
                await message.delete()
                await message.reply_sticker(
                    sticker=quotly.sticker.file_id,
                    reply_to_message_id=message.reply_to_message.id
                    if message.reply_to_message
                    else None,
                )
            else:
                return await message.edit("**Failed to Create Quotly Sticker**")
    await client.delete_messages(bot, 2)

@Ubot(["text"], cmds)
async def sticklet(client, message):
    reply_message = message.reply_to_message
    if not reply_message and len(message.text.split()) == 1:
        await message.edit("Please give a word or reply to a message.")
        return

    sticktext = reply_message.text if reply_message else message.text.split(" ", maxsplit=1)[1]
    if " " in sticktext:
        sticktext = sticktext.split(" ", maxsplit=1)[1]
    sticktext = textwrap.wrap(sticktext, width=10)
    sticktext = "\n".join(sticktext)

    color = "random"
    if len(message.text.split()) > 1 and message.text.split()[1].lower() in ["w", "r", "b", "g"]:
        color = message.text.split()[1].lower()

    if color == "w":
        R, G, B = 255, 255, 255
    elif color == "r":
        R, G, B = 255, 0, 0
    elif color == "b":
        R, G, B = 0, 0, 255
    elif color == "g":
        R, G, B = 0, 255, 0
    else:
        R = random.randint(0, 256)
        G = random.randint(0, 256)
        B = random.randint(0, 256)
        
    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    fontsize = 200
    font = ImageFont.truetype("cache/geezram.ttf", size=fontsize)
    
    while draw.multiline_textsize(sticktext, font=font) > (512, 512):
        fontsize -= 3
        font = ImageFont.truetype("cache/geezram.ttf", size=fontsize)
        
    width, height = draw.multiline_textsize(sticktext, font=font)
    draw.multiline_text(((512 - width) / 2, (512 - height) / 2), sticktext, font=font, fill=(R, G, B))
    
    image_stream = io.BytesIO()
    image_stream.name = "sticker.webp"
    image.save(image_stream, "webp")
    image_stream.seek(0)
    await message.delete()
    await client.send_sticker(
        chat_id=message.chat.id,
        sticker=image_stream,
        reply_to_message_id=message.message_id if reply_message else None
    )

@Ubot(["twitt"], cmds)
async def twitt(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.edit("**Please Reply to Message**")
    bot = "TwitterStatusBot"
    if message.reply_to_message:
        await message.edit("`Making a post...`")
        await client.unblock_user(bot)
        await message.reply_to_message.forward(bot)
        await asyncio.sleep(5)
        async for twitt in client.search_messages(bot, limit=1):
            if twitt:
                await message.delete()
                await message.reply_sticker(
                    sticker=twitt.sticker.file_id,
                    reply_to_message_id=message.reply_to_message.id
                    if message.reply_to_message
                    else None,
                )
            else:
                return await message.edit("**Failed to Create twitter status**")
                
    await client.delete_messages(bot, 2)

add_command_help(
    "qoute",
    [
        [f"q white [balas pesan]",
            "Membuat gambar quote dengan warna background." ],
    ],
)
