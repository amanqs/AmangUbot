# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

# Credits Tomi Setiawan
import asyncio
import os
import random
from io import BytesIO
import math
import shlex
from typing import Tuple
from pyrogram import Client, filters
from py_extract import Video_tools
from pyrogram.enums import MessageMediaType, MessagesFilter
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import InputMediaPhoto, Message
from ubotlibs.ubot.helper import get_arg
from . import *

async def dl_pic(client, download):
    path = await client.download_media(download)
    with open(path, "rb") as f:
        content = f.read()
    os.remove(path)
    get_photo = BytesIO(content)
    return get_photo

async def run_cmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )

mod_name = os.path.basename(__file__)[:-3]


@Ubot(["toaudio"], cmds)
async def extract_all_aud(client, message):
    replied_msg = message.reply_to_message
    babi = await message.reply("`Downloading Video . . .`")
    ext_out_path = os.getcwd() + "/" + "downloads/py_extract/audios"
    if not replied_msg:
        await babi.edit("**Mohon Balas Ke Video**")
        return
    if not replied_msg.video:
        await babi.edit("**Mohon Balas Ke Video**")
        return
    if os.path.exists(ext_out_path):
        await babi.edit("Processing.....")
        return
    replied_video = replied_msg.video
    try:
        await babi.edit("`Downloading...`")
        ext_video = await client.download_media(message=replied_video)
        await babi.edit("`Extracting Audio(s)...`")
        exted_aud = Video_tools.extract_all_audio(input_file=ext_video, output_path=ext_out_path)
        await babi.edit("`Uploading...`")
        for nexa_aud in exted_aud:
            await message.reply_audio(audio=nexa_aud, caption=f"`Extracted by` {(await client.get_me()).mention}")
        await babi.edit("`Extracting Finished!`")
        shutil.rmtree(ext_out_path)
    except Exception as e:
        await babi.edit(f"**Error:** `{e}`")


@Ubot("efek", cmds)
async def epek(client, message):
    helo = get_arg(message)
    rep = message.reply_to_message
    if rep and helo:
        tau = ["bengek", "robot", "jedug", "fast", "echo"]
        if helo in tau:
            Tm = await message.reply(f"Merubah suara menjadi {helo}")
            indir = await client.download_media(rep)
            KOMUT = {
                "bengek": '-filter_complex "rubberband=pitch=1.5"',
                "robot": "-filter_complex \"afftfilt=real='hypot(re,im)*sin(0)':imag='hypot(re,im)*cos(0)':win_size=512:overlap=0.75\"",
                "jedug": '-filter_complex "acrusher=level_in=8:level_out=18:bits=8:mode=log:aa=1"',
                "fast": "-filter_complex \"afftfilt=real='hypot(re,im)*cos((random(0)*2-1)*2*3.14)':imag='hypot(re,im)*sin((random(1)*2-1)*2*3.14)':win_size=128:overlap=0.8\"",
                "echo": '-filter_complex "aecho=0.8:0.9:500|1000:0.2|0.1"',
            }
            ses = await asyncio.create_subprocess_shell(
                f"ffmpeg -i '{indir}' {KOMUT[helo]} audio.mp3"
            )
            await ses.communicate()
            await Tm.delete()
            await rep.reply_voice("audio.mp3", caption=f"Efek {helo}")
            os.remove("audio.mp3")
        else:
            await message.reply(f"Silahkan isi sesuai {tau}")
    else:
        await Tm.edit(
            f"Silahkan balas ke audio atau mp3, contoh : <code>!efek bengek</code> sambil balas ke audio atau mp3"
        )
        
add_command_help(
    "convert",
    [
        [f"toaudio <reply to file>", "Convert video to audio."],
        [f"toanime <reply to foto>", "Convert foto ke anime menggunakan ai bot."],
        [f"togif <reply to video>", "Convert video ke gif."],
        [f"toimg <reply stiker>", "Convert stiker ke foto."],
        [f"cartoon [reply to image]", "Ubah gambar menggunakan deepai api."],
        [f"toonify [reply to image]", "Untuk mempercantik gambar menggunakan deepai api."],
        [f"pcil [reply to image]", "Untuk membuat gambar hitam putih."],
        [f"efek [reply to audio][bengek/robot/jedug/echo/fast]", "Untuk memberi efek pada audio."],
    ],
)

