# Credits : @Xtsea
# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


from . import *

import random

import glob

import os

from PIL import Image, ImageDraw, ImageFont

from pyrogram import Client, filters

from pyrogram import Client, filters, enums
from Ubot.core.lgs import *
from . import *

@Ubot(["logo2"], cmds)

async def logo_gen(client, message):

    xx = await message.reply_text("`Mempersiapkan logo Anda...`")

    name = message.text.split(" ", 1)[1]

    if not name:

        await xx.edit("`Sediakan beberapa teks untuk digambar!\nContoh: /logo <nama Anda>!`")

        return

    bg_, font_ = "", ""

    if message.reply_to_message:

        temp = message.reply_to_message

        if temp.media:

            if temp.document:

                if "font" in temp.document.mime_type:

                    font_ = await temp.download()

                elif (".ttf" in temp.document.file_name) or (".otf" in temp.document.file_name):

                    font_ = await temp.download()

            elif temp.photo:

                bg_ = await temp.download()

    else:

        pics = []

        async for i in client.search_messages("AllLogoHyper", filter=enums.MessagesFilter.PHOTO

                ):

            if i.photo:

                pics.append(i)

        id_ = random.choice(pics)

        bg_ = await id_.download()

        fpath_ = glob.glob("Ubot/resources/fonts/*")

        font_ = random.choice(fpath_)

    if not bg_:

        pics = []

        async for i in client.search_messages("AllLogoHyper", filter=enums.MessagesFilter.PHOTO

                ):

            if i.photo:

                pics.append(i)

        id_ = random.choice(pics)

        bg_ = await id_.download()

    if not font_:

        fpath_ = glob.glob("Ubot/resources/fonts/*")

        font_ = random.choice(fpath_)

    if len(name) <= 8:

        fnt_size = 120

        strke = 10

    elif len(name) >= 9:

        fnt_size = 50

        strke = 5

    else:

        fnt_size = 100

        strke = 20

    img = Image.open(bg_)

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(font_, fnt_size)

    w, h = draw.textsize(name, font=font)

    h += int(h * 0.21)

    image_width, image_height = img.size

    draw.text(

        ((image_width - w) / 2, (image_height - h) / 2),

        name,

        font=font,

        fill=(255, 255, 255),

    )

    x = (image_width - w) / 2

    y = (image_height - h) / 2

    draw.text((x, y), name, font=font, fill="white",

              stroke_width=strke, stroke_fill="black")

    flnme = f"logo.png"

    img.save(flnme, "png")

    await xx.edit("`Uploading`")

    if os.path.exists(flnme):

        await client.send_photo(

            chat_id=message.chat.id,

            photo=flnme,

            caption=f"Logo by {client.me.mention}",

        )

        os.remove(flnme)

        await xx.delete()

    if os.path.exists(bg_):

        os.remove(bg_) 

    if os.path.exists(font_):

        if not font_.startswith("Ubot/resources/fonts"):

            os.remove(font_)



@Ubot("logo", cmds)
async def logo_command(client, message):
    await logo_write(client, message)


add_command_help(

    "logo",

    [

        [f"logo [kata]", "Buat Logo Secara Random."],

        [f"logo2 [kata]", "Buat Logo Secara Random."],

    ],

)
