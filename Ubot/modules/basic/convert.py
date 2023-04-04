# Credits Tomi Setiawan
import asyncio
import os
import random
from io import BytesIO
import math
import shlex
from typing import Tuple
from pyrogram import Client, filters
from pyrogram.enums import MessageMediaType, MessagesFilter
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import InputMediaPhoto
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


@Client.on_message(filters.command("toaudio", ".") & filters.me)
async def audio(client, message):
    replied = message.reply_to_message
    Tm = await message.reply("<b>Tunggu sebentar</b>")
    if not replied:
        return await Tm.edit("<b>Mohon Balas Ke Video</b>")
    if replied.media == MessageMediaType.VIDEO:
        await Tm.edit("<b>Downloading Video . . .</b>")
        file = await client.download_media(
            message=replied,
            file_name=f"audio{random.choice(range(9999999))}/",
        )
        out_file = f"{file}.mp3"
        try:
            await Tm.edit("<b>Mencoba Ekstrak Audio. . .</b>")
            cmd = f"ffmpeg -i {file} -q:a 0 -map a {out_file}"
            await run_cmd(cmd)
            await Tm.edit("<b>Uploading Audio . . .</b>")
            await client.send_voice(
                message.chat.id,
                voice=out_file,
                reply_to_message_id=message.id,
            )
            os.remove(out_file)
            await Tm.delete()
        except Exception as error:
            await Tm.edit(error)
    else:
        return await Tm.edit("<b>Mohon Balas Ke Video</b>")


@Ubot("efek", "")
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

