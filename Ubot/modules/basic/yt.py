# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT



import asyncio
import os
import time
from datetime import datetime
from urllib.request import urlretrieve

import wget
import os, pytube, requests
from pyrogram import *
from pyrogram.types import *
from youtube_search import YoutubeSearch
from pytube import YouTube

from ubotlibs.ubot.helper.PyroHelpers import ReplyCheck
from ubotlibs.ubot.utils.tools import *
from pyrogram import Client, enums
from pyrogram.types import Message
from pyrogram.errors import YouBlockedUser
from . import *


CAPTION_TEXT = """
 **Title:** `{}`
 **Requester** : {}
 **Downloaded Via** : `{}`
"""

async def downloadsong(m, message, vid_id):
    try: 
        m = await m.edit(text = f"📥 **Download**")
        link =  YouTube(f"https://youtu.be/{vid_id}")
        title = link.title
        thumbloc = f"downloads/{title}.jpg"
        thumb = requests.get(link.thumbnail_url, allow_redirects=True)
        open(thumbloc , 'wb').write(thumb.content)
        songlink = link.streams.filter(only_audio=True).first()
        down = songlink.download(output_path="downloads/")
        first, last = os.path.splitext(down)
        song = first + '.mp3'
        os.rename(down, song)
        m = await m.edit(text = """
📤 **Upload Started**
        """)
        await message.reply_audio(audio=song,
            caption = f"{title}\n\n{CAPTION_TEXT.format(link.title, message.from_user.mention if message.from_user else 'Anonymous Admin', 'Youtube')}",
            thumb=thumbloc)
        await m.delete()
        if os.path.exists(song):
            os.remove(song)
        if os.path.exists(thumbloc):
            os.remove(thumbloc)
    except Exception as e:
        await m.edit(f"Terjadi kesalahan. ⚠️ \nAnda juga bisa mendapatkan bantuan dari @amwangsupport.__\n\n{str(e)}")
        
    except HTTPError as e:
       if e.status_code == 429:
           time.sleep(3)
           return await downloadsong(m, message, vid_id)
       else:
           raise e

async def downlodvideo(m, message, vid_id):
   try: 
    m = await m.edit(text = "📥 Downloading...",)
    link =  YouTube(f"https://youtu.be/{vid_id}")
    videolink = link.streams.get_highest_resolution()
    video = videolink.download(output_path="downloads/")
    m = await m.edit(text = "📤 Uploading...")
    await message.reply_video(video, 
    caption=CAPTION_TEXT.format(link.title, message.from_user.mention if message.from_user else "Anonymous Admin", "Youtube"))
    await m.delete()
    if os.path.exists(video):
            os.remove(video)
   except Exception as e:
       await m.edit(f"`Terjadi kesalahan. ⚠️ \nAnda juga bisa mendapatkan bantuan dari @amwangsupport.__\n\n{str(e)}`")
       
   except HTTPError as e:
       if e.status_code == 429:
           time.sleep(3)
           return await downloadvideo(m, message, vid_id)
       else:
           raise e


@Ubot("song2", cmds)
async def songdown(client: Client, message: Message):
   try: 
    if len(message.command) < 2:
            return await message.reply_text("`Beri nama lagu ⚠️`")
    m = await message.reply_text("🔎 Mencari ...")
    name = message.text.split(None, 1)[1]
    vid_id = (YoutubeSearch(name, max_results=1).to_dict())[0]["id"]
    await downloadsong(m, message, vid_id)
   except Exception as e:
       await m.edit(f"""
**Tidak ditemukan** {message.from_user.mention}   
Silakan periksa, Anda menggunakan format yang benar atau ejaan Anda benar dan coba lagi!
       """)


@Ubot(["vid2", "video2"], cmds)
async def videodown(client: Client, message: Message):
   try: 
    if len(message.command) < 2:
            return await message.reply_text("`Beri nama lagu ⚠️`")
    m = await message.reply_text("`🔎 Mencari ...`")
    name = message.text.split(None, 1)[1]
    vid_id = (YoutubeSearch(name, max_results=1).to_dict())[0]["id"]
    await downlodvideo(m, message, vid_id)
   except Exception:
       await m.edit(f"""
**Tidak ditemukan** {message.from_user.mention}   
Silakan periksa, Anda menggunakan format yang benar atau ejaan Anda benar dan coba lagi!
       """)
            
            
@Ubot(["sosmed"], cmds)
async def sosmed(client: Client, message: Message):
    prik = await message.edit("`Processing . . .`")
    link = get_arg(message)
    bot = "thisvidbot"
    if link:
        try:
            tuyul = await client.send_message(bot, link)
            await asyncio.sleep(5)
            await tuyul.delete()
        except YouBlockedUser:
            await client.unblock_user(bot)
            tuyul = await client.send_message(bot, link)
            await asyncio.sleep(5)
            await tuyul.delete()
    async for sosmed in client.search_messages(
        bot, filter=enums.MessagesFilter.VIDEO, limit=1
    ):
        await asyncio.gather(
            prik.delete(),
            client.send_video(
                message.chat.id,
                sosmed.video.file_id,
                caption=f"**Upload by:** {client.me.mention}",
                reply_to_message_id=ReplyCheck(message),
            ),
        )
        await client.delete_messages(bot, 2)


add_command_help(
    "youtube",
    [
        [f"song <judul>", "Download Audio From YouTube."],
        [f"vid atau video <judul>", "Download Video from YouTube."],
    ],
)

add_command_help(
    "sosmed",
    [
        [
            f"sosmed/tt/ig <link>",
            "Untuk Mendownload Media Dari Facebook / Tiktok / Instagram / Twitter / YouTube.",
        ],
    ],
)
