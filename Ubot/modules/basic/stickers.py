# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

import asyncio
import os
import random
from io import BytesIO

import shlex
import textwrap
import cv2
import requests
from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup as bs
from pyrogram import Client, emoji, filters
from pyrogram.enums import ParseMode
from pyrogram.errors import StickersetInvalid, YouBlockedUser
from pyrogram.raw.functions.messages import GetStickerSet
from pyrogram.raw.types import InputStickerSetShortName
from pyrogram.types import Message, InputMedia, InputMediaPhoto

from . import *
from ubotlibs.ubot.helper.PyroHelpers import ReplyCheck
from ubotlibs.ubot.utils import *


sat= [
    "Ijin nyolong banh..",
    "Buset maling ah...",
    "Sststststs Dor...",
    "Woy, Ijin maling banh..",
    "Minta dong banh ...",
]
"""
@Client.on_message(filters.command(["pack"], cmds) & filters.me)
def create_pack(client, message):
    biji = message.text.split(' ')
    if len(biji) < 2:
        message.edit_text("Kirim perintah dengan format pack [nama pack]")
        return
    pack_name = biji[1]

    if not message.reply_to_message or not message.reply_to_message.sticker:
        message.edit_text("Balas pesan stiker untuk ditambahkan ke pack sticker.")
        return
    
    sticker_file_id = message.reply_to_message.sticker.file_id
    
    try:
        pack = client.create_new_sticker_set(
            user_id=message.from_user.id,
            name=pack_name,
            title=pack_name,
            emojis="👍",
            png_sticker=sticker_file_id
        )
    except ValueError as e:
        if str(e) == "Stickerset_invalid":
            message.edit_text(f"Sticker pack {pack_name} sudah ada, tambahkan stiker lainnya ke pack.")
            return
        else:
            raise e
        
    message.edit_text(f"Sticker pack {pack_name} telah berhasil dibuat.")
"""



@Ubot(["kang"], cmds)
async def kang(client: Client, message: Message):
    user = client.me
    replied = message.reply_to_message
    um = await message.edit_text(random.choice(sat))
    media_ = None
    emoji_ = None
    is_anim = False
    is_video = False
    resize = False
    ff_vid = False
    if replied and replied.media:
        if replied.photo:
            resize = True
        elif replied.document and "image" in replied.document.mime_type:
            resize = True
            replied.document.file_name
        elif replied.document and "tgsticker" in replied.document.mime_type:
            is_anim = True
            replied.document.file_name
        elif replied.document and "video" in replied.document.mime_type:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.animation:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.video:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.sticker:
            if not replied.sticker.file_name:
                await um.edit("**The sticker has no Name!**")
                return
            emoji_ = replied.sticker.emoji
            is_anim = replied.sticker.is_animated
            is_video = replied.sticker.is_video
            if not (
                replied.sticker.file_name.endswith(".tgs")
                or replied.sticker.file_name.endswith(".webm")
            ):
                resize = True
                ff_vid = True
        else:
            await um.edit("**Unsupported Files**")
            return
        media_ = await client.download_media(replied, file_name="Ubot/resources/")
    else:
        await um.edit("**Please Reply to Photo/GIF/Sticker Media!**")
        return
    if media_:
        args = get_arg(message)
        pack = 1
        if len(args) == 2:
            emoji_, pack = args
        elif len(args) == 1:
            if args[0].isnumeric():
                pack = int(args[0])
            else:
                emoji_ = args[0]

        if emoji_ and emoji_ not in (
            getattr(emoji, _) for _ in dir(emoji) if not _.startswith("_")
        ):
            emoji_ = None
        if not emoji_:
            emoji_ = "✨"

        u_name = user.username
        u_name = "@" + u_name if u_name else user.first_name or user.id
        packname = f"Sticker_u{user.id}_v{pack}"
        custom_packnick = f"{u_name} Sticker Pack"
        packnick = f"{custom_packnick} Vol.{pack}"
        cmd = "/newpack"
        if resize:
            media_ = await resize_media(media_, is_video, ff_vid)
        if is_anim:
            packname += "_animated"
            packnick += " (Animated)"
            cmd = "/newanimated"
        if is_video:
            packname += "_video"
            packnick += " (Video)"
            cmd = "/newvideo"
        exist = False
        while True:
            try:
                exist = await client.invoke(
                    GetStickerSet(
                        stickerset=InputStickerSetShortName(short_name=packname), hash=0
                    )
                )
            except StickersetInvalid:
                exist = False
                break
            limit = 50 if (is_video or is_anim) else 120
            if exist.set.count >= limit:
                pack += 1
                packname = f"a{user.id}_by_userge_{pack}"
                packnick = f"{custom_packnick} Vol.{pack}"
                if is_anim:
                    packname += f"_anim{pack}"
                    packnick += f" (Animated){pack}"
                if is_video:
                    packname += f"_video{pack}"
                    packnick += f" (Video){pack}"
                await um.edit(
                    f"`Create a New Sticker Pack {pack} Because the Sticker Pack Is Full`"
                )
                continue
            break
        if exist is not False:
            try:
                await client.send_message("stickers", "/addsticker")
            except YouBlockedUser:
                await client.unblock_user("stickers")
                await client.send_message("stickers", "/addsticker")
            except Exception as e:
                return await Man.edit(f"**ERROR:** `{e}`")
            await asyncio.sleep(2)
            await client.send_message("stickers", packname)
            await asyncio.sleep(2)
            limit = "50" if is_anim else "120"
            while limit in await get_response(message, client):
                pack += 1
                packname = f"a{user.id}_by_{user.username}_{pack}"
                packnick = f"{custom_packnick} vol.{pack}"
                if is_anim:
                    packname += "_anim"
                    packnick += " (Animated)"
                if is_video:
                    packname += "_video"
                    packnick += " (Video)"
                await um.edit(
                    "`Create a New Sticker Pack "
                    + str(pack)
                    + " Because the sticker pack is full`"
                )
                await client.send_message("stickers", packname)
                await asyncio.sleep(2)
                if await get_response(message, client) == "Invalid pack selected.":
                    await client.send_message("stickers", cmd)
                    await asyncio.sleep(2)
                    await client.send_message("stickers", packnick)
                    await asyncio.sleep(2)
                    await client.send_document("stickers", media_)
                    await asyncio.sleep(2)
                    await client.send_message("Stickers", emoji_)
                    await asyncio.sleep(2)
                    await client.send_message("Stickers", "/publish")
                    await asyncio.sleep(2)
                    if is_anim:
                        await client.send_message(
                            "Stickers", f"<{packnick}>", parse_mode=ParseMode.MARKDOWN
                        )
                        await asyncio.sleep(2)
                    await client.send_message("Stickers", "/skip")
                    await asyncio.sleep(2)
                    await client.send_message("Stickers", packname)
                    await asyncio.sleep(2)
                    await um.edit(
                        f"**Sticker Added Successfully!**\n**[CLICK HERE](https://t.me/addstickers/{packname})**"
                    )
                    return
            await client.send_document("stickers", media_)
            await asyncio.sleep(2)
            if (
                await get_response(message, client)
                == "Sorry, the file type is invalid."
            ):
                await um.edit(
                    "**Failed to Add Sticker, Use @Stickers Bot To Add Your Sticker.**"
                )
                return
            await client.send_message("Stickers", emoji_)
            await asyncio.sleep(2)
            await client.send_message("Stickers", "/done")
        else:
            await um.edit("`Create a New Sticker Pack`")
            try:
                await client.send_message("Stickers", cmd)
            except YouBlockedUser:
                await client.unblock_user("stickers")
                await client.send_message("stickers", "/addsticker")
            await asyncio.sleep(2)
            await client.send_message("Stickers", packnick)
            await asyncio.sleep(2)
            await client.send_document("stickers", media_)
            await asyncio.sleep(2)
            if (
                await get_response(message, client)
                == "Sorry, the file type is invalid."
            ):
                await um.edit(
                    "**Failed to Add Sticker, Use @Stickers Bot To Add Your Sticker.**"
                )
                return
            await client.send_message("Stickers", emoji_)
            await asyncio.sleep(2)
            await client.send_message("Stickers", "/publish")
            await asyncio.sleep(2)
            if is_anim:
                await client.send_message("Stickers", f"<{packnick}>")
                await asyncio.sleep(2)
            await client.send_message("Stickers", "/skip")
            await asyncio.sleep(2)
            await client.send_message("Stickers", packname)
            await asyncio.sleep(2)
        await um.edit(
            f"**Sticker Added Successfully!**\n**[CLICK HERE](https://t.me/addstickers/{packname})**"
        )
        if os.path.exists(str(media_)):
            os.remove(media_)


async def get_response(message, client):
    return [x async for x in client.get_chat_history("Stickers", limit=1)][0].text


@Ubot(["packinfo"], cmds)
async def packinfo(client: Client, message: Message):
    rep = await message.edit_text("`Processing...`")
    if not message.reply_to_message:
        await rep.edit("Please Reply To Sticker...")
        return
    if not message.reply_to_message.sticker:
        await rep.edit("Please Reply To A Sticker...")
        return
    if not message.reply_to_message.sticker.set_name:
        await rep.edit("`Seems Like A Stray Sticker!`")
        return
    stickerset = await client.invoke(
        GetStickerSet(
            stickerset=InputStickerSetShortName(
                short_name=message.reply_to_message.sticker.set_name
            ),
            hash=0,
        )
    )
    emojis = []
    for stucker in stickerset.packs:
        if stucker.emoticon not in emojis:
            emojis.append(stucker.emoticon)
    output = f"""**Sticker Pack Title **: `{stickerset.set.title}`
**Sticker Pack Short Name **: `{stickerset.set.short_name}`
**Stickers Count **: `{stickerset.set.count}`
**Archived **: `{stickerset.set.archived}`
**Official **: `{stickerset.set.official}`
**Masks **: `{stickerset.set.masks}`
**Animated **: `{stickerset.set.animated}`
**Emojis In Pack **: `{' '.join(emojis)}`
"""
    await rep.edit(output)


@Ubot(["stickers"], cmds)
async def cb_sticker(client: Client, message: Message):
    query = get_text(message)
    if not query:
        return await message.edit_text("**Enter the name of the Sticker Pack!**")
    xx = await message.edit_text(message, "`Searching sticker packs...`")
    text = requests.get(f"https://combot.org/telegram/stickers?q={query}").text
    soup = bs(text, "lxml")
    results = soup.find_all("div", {"class": "sticker-pack__header"})
    if not results:
        return await xx.edit("**Cannot Find Sticker Pack 🥺**")
    reply = f"**Keyword Sticker Pack:**\n {query}\n\n**Results:**\n"
    for pack in results:
        if pack.button:
            packtitle = (pack.find("div", "sticker-pack__title")).get_text()
            packlink = (pack.a).get("href")
            reply += f" •  [{packtitle}]({packlink})\n"
    await xx.edit(reply)


@Ubot(["tiny"], cmds)
async def tinying(client: Client, message: Message):
    reply = message.reply_to_message
    if not (reply and (reply.media)):
        return await message.edit_text("**Please Reply To Sticker Message!**")
    tex = await message.edit_text("`Processing . . .`")
    ik = await client.download_media(reply)
    im1 = Image.open("Ubot/resources/blank.png")
    if ik.endswith(".tgs"):
        await client.download_media(reply, "man.tgs")
        await bash("lottie_convert.py man.tgs json.json")
        json = open("json.json", "r")
        jsn = json.read()
        jsn = jsn.replace("512", "2000")
        ("json.json", "w").write(jsn)
        await bash("lottie_convert.py json.json man.tgs")
        file = "man.tgs"
        os.remove("json.json")
    elif ik.endswith((".gif", ".mp4")):
        iik = cv2.VideoCapture(ik)
        busy = iik.read()
        cv2.imwrite("i.png", busy)
        fil = "i.png"
        im = Image.open(fil)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove(fil)
        os.remove("k.png")
    else:
        im = Image.open(ik)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove("k.png")
    await asyncio.gather(
        tex.delete(),
        client.send_sticker(
            message.chat.id,
            sticker=file,
            reply_to_message_id=ReplyCheck(message),
        ),
    )
    os.remove(file)
    os.remove(ik)


@Ubot(["mmf"], cmds)
async def memify(client: Client, message: Message):
    if not message.reply_to_message_id:
        await message.edit_text("**Mohon balas ke stikers!**")
        return
    reply_message = message.reply_to_message
    if not reply_message.media:
        await message.text("**Mohon balas ke stikers!**")
        return
    file = await client.download_media(reply_message)
    mm = await message.edit_text("`Processing . . .`")
    text = get_arg(message)
    if len(text) < 1:
        return await mm.edit("`Please Type `.mmf text")
    meme = await add_text_img(file, text)
    await asyncio.gather(
        mm.delete(),
        client.send_sticker(
            message.chat.id,
            sticker=meme,
            reply_to_message_id=ReplyCheck(message),
        ),
    )
    os.remove(meme)


@Ubot(["toimg"], cmds)
async def stick2png(client: Client, message: Message):
    try:
        await message.edit("`Downloading . . .`")

        path = await message.reply_to_message.download()
        with open(path, "rb") as f:
            content = f.read()
        os.remove(path)

        file_io = BytesIO(content)
        file_io.name = "sticker.png"

        await asyncio.gather(
            message.delete(),
            client.send_photo(
                message.chat.id,
                file_io,
                reply_to_message_id=ReplyCheck(message),
            ),
        )
    except Exception as e:
        return await client.send_message(
            message.chat.id, f"**INFO:** `{e}`", reply_to_message_id=ReplyCheck(message)
        )


add_command_help(
    "sticker",
    [
        [f"kang `Balas` Gambar",
            f"Balas kang menambahkan gambar/stiker ke pack stiker anda."],
        [f"kang [emoji] `atau` double [emoji]",
            "Menambahkan stiker dengan spesifik emoji.`"],
        [f"packinfo `or` stickerinfo",
            "Mengambil info stiker atau pack striker."],
        [f"stickers <nama sticker>", "Untuk mencari pack stikernya."],
    ],
)


add_command_help(
    "meme",
    [
        [f"mmf Top Text ; Bottom Text",
            "Balas ke stiker untuk membuat memify text stiker."],
        [f"tiny [reply ke photo/sticker]",
            "To Change the Sticker to be Small."],
        [f"text <warna>/<r/g/b/w> <pesan> atau <balas ke pesan>",
            "Merubah text jadi sticker."],
        [f"twitt <balas ke pesan>",
            "Mebuat stiker status twitter."],
        [f"mms atau meme <teks>",
            "Mebuat stiker random dengan text."],
    ],
)

