# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import os
import time
import random
import string
import asyncio
import time
import datetime
import threading

import logging
import ffmpeg
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, MessageNotModified
from pytgcalls import GroupCallFactory, GroupCallFileAction
from yt_dlp import YoutubeDL
from youtubesearchpython import SearchVideos
from ubotlibs.ubot.utils.tools import get_text, humanbytes, run_in_exc, run_cmd
from ubotlibs.ubot.helper.basic import edit_or_reply
from . import *


s_dict = {}
GPC = {}


@Ubot(["playlist"], cmds)
async def pl(client, message):
    group_call = GPC.get((message.chat.id, client.me.id))
    play = await message.reply("**Processing**")
    song = f"**📋 Daftar Playlist {message.chat.title}** : \n"
    s = s_dict.get((message.chat.id, client.me.id))
    if not group_call:
        return await play.edit("**Obrolan Suara Tidak Ditemukan**")
    if not s:
        if group_call.is_connected:
            return await play.edit(f"**📀 Sedang diputar :** `{group_call.song_name}**")
        else:
            return await play.edit("**Obrolan Suara Tidak Ditemukan**")
    if group_call.is_connected:
        song += f"**📀 Sedang diputar :** `{group_call.song_name}` \n\n"
    for sno, i in enumerate(s, start=1):
        song += f"**{sno} 🎧** [{i['song_name']}]({i['url']}) `| {i['singer']} | {i['dur']}` \n\n"
    await play.edit(song, disable_web_page_preview=True)
    
async def get_chat_(client, chat_):
    chat_ = str(chat_)
    if chat_.startswith("-100"):
        try:
            return (await client.get_chat(int(chat_))).id
        except ValueError:
            chat_ = chat_.split("-100")[1]
            chat_ = '-' + str(chat_)
            return int(chat_)
        
async def playout_ended_handler(group_call, filename):
    client_ = group_call.client
    chat_ = await get_chat_(client_, f"-100{group_call.full_chat.id}")
    chat_ = int(chat_)
    s = s_dict.get((chat_, client_.me.id))
    if os.path.exists(group_call.input_filename):
        os.remove(group_call.input_filename)
    if not s:
        await group_call.stop()
        del GPC[(chat_, client_.me.id)]
        return
    name_ = s[0]['song_name']
    singer_ = s[0]['singer']
    dur_ = s[0]['dur']
    raw_file = s[0]['raw']
    link = s[0]['url']
    file_size = humanbytes(os.stat(raw_file).st_size)
    song_info = f'📌 <b>Sedang dimainkan</b> \n📀 <b>Judul:</b> <a href="{link}">{name_}</a> \n🎸 <b>Artis:</b> <code>{singer_}</code> \n⏲️ <b>Waktu:</b> <code>{dur_}</code> \n📂 <b>Ukuran:</b> <code>{file_size}</code>'
    await client_.send_message(
        chat_, 
        song_info,
        disable_web_page_preview=True,
    )
    s.pop(0)
    logging(song_info)
    group_call.song_name = name_
    group_call.input_filename = raw_file


@Ubot(["skip"], cmds)
async def skip_m(client, message):
    group_call = GPC.get((message.chat.id, client.me.id))
    s_d = s_dict.get((message.chat.id, client.me.id))
    if not group_call:
        return await message.reply_text("**Tidak sedang memutar apa-apa!**")
    if not s_d:
        return await message.edit_text("**Antrian kosong!**")
    next_song = s_d.pop(0)
    raw_file_name = next_song["raw"]
    vid_title = next_song["song_name"]
    uploade_r = next_song["singer"]
    dur = next_song["dur"]
    url = next_song["url"]
    if os.path.exists(raw_file_name):
        group_call.input_filename = raw_file_name
        group_call.song_name = vid_title
        return await message.edit_text(f"📌 **Memutar Lagu Berikutnya**\n📀 **Judul**: `{vid_title}`\n💌 **Artis**: `{uploade_r}`")
    else:
        start = time.time()
        try:
            audio_original = await yt_dl(url, client, message, start)
        except BaseException as e:
            return await message.edit_text(f"**Kesalahan** \n**Error :** `{str(e)}**")
        try:
            raw_file_name = await convert_to_raw(audio_original, raw_file_name)
        except BaseException as e:
            return await message.edit_text(f"**Kesalahan..** \n**Error :** `{e}**")
        if os.path.exists(audio_original):
            os.remove(audio_original)
        group_call.input_filename = raw_file_name
        group_call.song_name = vid_title
        return await message.edit_text(f"📌 **Memutar Lagu Berikutnya**\n📀 **Judul**: {vid_title}\n💌 **Artis**: {uploade_r}")



@Ubot(["play"], cmds)
async def play_m(client, message):
    group_call = GPC.get((message.chat.id, client.me.id))
    u_s = await message.edit_text("**Processing..**")
    input_str = get_text(message)
    if not input_str:
        if not message.reply_to_message:
            return await u_s.edit_text("**Berikan Judul Lagu/Balas Ke File Audio..**")
        if not message.reply_to_message.audio:
            return await u_s.edit_text("**Berikan Judul Lagu/Balas Ke File Audio..**")
        audio = message.reply_to_message.audio
        audio_original = await message.reply_to_message.download()
        vid_title = audio.title or audio.file_name
        uploade_r = message.reply_to_message.audio.performer or "Unknown Artist."
        dura_ = message.reply_to_message.audio.duration
        dur = datetime.timedelta(seconds=dura_)
        raw_file_name = (
            ''.join(random.choice(string.ascii_lowercase) for i in range(5))
            + ".raw"
        )

        url = message.reply_to_message.link
    else:
        search = SearchVideos(str(input_str), offset=1, mode="dict", max_results=1)
        rt = search.result()
        result_s = rt.get("search_result")
        if not result_s:
           return await u_s.edit(f"**Lagu tidak ditemukan** {input_str}")
        url = result_s[0]["link"]
        dur = result_s[0]["duration"]
        vid_title = result_s[0]["title"]
        yt_id = result_s[0]["id"]
        uploade_r = result_s[0]["channel"]
        start = time.time()
        try:
           audio_original = await yt_dl(url, client, message, start)
        except BaseException as e:
           return await u_s.edit(f"**Error :** `{str(e)}**")
        raw_file_name = (
            ''.join(random.choice(string.ascii_lowercase) for i in range(5))
            + ".raw"
        )

    try:
        raw_file_name = await convert_to_raw(audio_original, raw_file_name)
    except BaseException as e:
        return await u_s.edit(f"**Error :** `{e}**")
    if os.path.exists(audio_original):
        os.remove(audio_original)
    if not group_call:
        group_call = GroupCallFactory(client).get_file_group_call()
        group_call.song_name = vid_title
        GPC[(message.chat.id, client.me.id)] = group_call
        try:
            await group_call.start(message.chat.id)
        except BaseException as e:
            return await u_s.edit(f"**Error:** `{e}**")
        group_call.add_handler(playout_ended_handler, GroupCallFileAction.PLAYOUT_ENDED)
        group_call.input_filename = raw_file_name
        return await u_s.edit(f"🔖 **Sedang memainkan** \n📀 **Judul**: `{vid_title}`\n 💌 **Group**: {message.chat.title}")
    elif not group_call.is_connected:
        try:
            await group_call.start(message.chat.id)
        except BaseException as e:
            return await u_s.edit(f"**Error:** `{e}`")
        group_call.add_handler(playout_ended_handler, GroupCallFileAction.PLAYOUT_ENDED)
        group_call.input_filename = raw_file_name
        group_call.song_name = vid_title
        return await u_s.edit(f"🔖 **Sedang memainkan** \n📀 **Judul**: `{vid_title}`\n 💌 **Group**: {message.chat.title}")
    else:
        s_d = s_dict.get((message.chat.id, client.me.id))
        f_info = {"song_name": vid_title,
                  "raw": raw_file_name,
                  "singer": uploade_r,
                  "dur": dur,
                  "url": url
                 }
        if s_d:
            s_d.append(f_info)
        else:
            s_dict[(message.chat.id, client.me.id)] = [f_info]
        s_d = s_dict.get((message.chat.id, client.me.id))
        return await u_s.edit(f"✚ **Ditambahkan ke antrian**\n 🔖 **Judul**: {vid_title}\n 📑 **Di posisi**: #{len(s_d)+1}")


@run_in_exc
def convert_to_raw(audio_original, raw_file_name):
    ffmpeg.input(audio_original).output(raw_file_name, format="s16le", acodec="pcm_s16le", ac=2, ar="48k", loglevel="error").overwrite_output().run()
    return raw_file_name

def edit_msg(client, message, to_edit):
    try:
        client.loop.create_task(message.edit(to_edit))
    except MessageNotModified:
        pass
    except FloodWait as e:
        client.loop.create_task(asyncio.sleep(e.x))
    except TypeError:
        pass
    
def download_progress_hook(d, message, client, start):
    if d['status'] == 'downloading':
        current = d.get("_downloaded_bytes_str") or humanbytes(d.get("downloaded_bytes", 1))
        total = d.get("_total_bytes_str") or d.get("_total_bytes_estimate_str")
        file_name = d.get("filename")
        eta = d.get('_eta_str', "N/A")
        percent = d.get("_percent_str", "N/A")
        speed = d.get("_speed_str", "N/A")
        to_edit = f"<b>🔄 Processing</b>"
        threading.Thread(target=edit_msg, args=(client, message, to_edit)).start()

@run_in_exc
def yt_dl(url, client, message, start):
    opts = {
             "format": "bestaudio",
             "addmetadata": True,
             "key": "FFmpegMetadata",
             "prefer_ffmpeg": True,
             "geo_bypass": True,
             "progress_hooks": [lambda d: download_progress_hook(d, message, client, start)],
             "nocheckcertificate": True,
             "postprocessors": [
                 {
                     "key": "FFmpegExtractAudio",
                     "preferredcodec": "mp3"
                 }
             ],
             "outtmpl": "%(id)s",
             "quiet": True,
             "logtostderr": False,
         }
    with YoutubeDL(opts) as ytdl:
        ytdl_data = ytdl.extract_info(url, download=True)
    return str(ytdl_data['id']) + ".mp3"

RD_ = {}
FFMPEG_PROCESSES = {}


@Ubot(["pause"], cmds)
async def no_song_play(client, message):
    group_call = GPC.get((message.chat.id, client.me.id))
    if not group_call:
        await message.reply_text("**Tidak Ada Pemutaran**")
        return
    if not group_call.is_connected:
        await message.edit_text("**Tidak Ada Pemutaran**")
        return    
    await message.edit_text(f"⏸ **Dijeda.** {str(group_call.input_filename).replace('.raw', '')}.")
    group_call.pause_playout()
    

@Ubot(["resume"], cmds)
async def wow_dont_stop_songs(client, message):
    group_call = GPC.get((message.chat.id, client.me.id))
    if not group_call:
        await message.reply_text("**Tidak Ada Pemutaran**")
        return    
    if not group_call.is_connected:
        await message.edit_text("**Tidak Ada Pemutaran**")
        return    
    group_call.resume_playout()
    await message.edit_text("▶️**Dilanjutkan.**")
        

@Ubot(["end"], cmds)
async def leave_vc_test(client, message):
    group_call = GPC.get((message.chat.id, client.me.id))
    if not group_call:
        await message.reply_text("**Tidak Ada Pemutaran**")
        return
    if not group_call.is_connected:
        await message.edit_text("**Tidak Ada Pemutaran**")
        return
    if os.path.exists(group_call.input_filename):
        os.remove(group_call.input_filename)
    await group_call.stop()
    await message.edit_text(f"❌ **Lagu Dihentikan Di**  {message.chat.title}")
    del GPC[(message.chat.id, client.me.id)]
    
add_command_help(
    "music",
    [
        [f"play", "Play Musik & Video Dengan Judul Lagu."],
        [f"skip", "Skip Lagu."],
        [f"pause", "Pause Musik."],
        [f"resume", "Resume Musik."],
        [f"end", "Stop Musik."],
        [f"playlist", "Play Playlist Musik."],
    ],
)
