
import time
import random
import speedtest
import asyncio
import re
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message
from datetime import datetime
from . import *
from ubotlibs.ubot.helper.PyroHelpers import *
from Ubot import *
from Ubot.core.db import set_prefix, get_prefix
from .systemstats import get_readable_time
from ubotlibs.ubot.utils.tools import get_arg


async def edit_or_reply(message: Message, *args, **kwargs) -> Message:
    apa = (
        message.edit_text
        if bool(message.from_user and message.from_user.is_self or message.outgoing)
        else (message.reply_to_message or message).reply_text
    )
    return await apa(*args, **kwargs)


eor = edit_or_reply


class WWW:
    SpeedTest = (
        "Speedtest started at `{start}`\n"
        "Ping ➠ `{ping}` ms\n"
        "Download ➠ `{download}`\n"
        "Upload ➠ `{upload}`\n"
        "ISP ➠ __{isp}__"
    )

    NearestDC = "Country: `{}`\n" "Nearest Datacenter: `{}`\n" "This Datacenter: `{}`"
    
kopi = [
    "**Hadir Mas** 😍",
    "**Mmuaahh** 😘",
    "**Hadir** 🤗",
    "**Kenapa Mas** 🥰",
    "**Iya Mas Kenapa?** 😘",
    "**Dalem Mas** 🤗",
    "**Aku Mas ?**",
]
    
    
@Ubot(["speed"], "")
async def speed_test(client: Client, message: Message):
    new_msg = await message.reply_text("`Running speed test . . .`")
    try:
       await message.delete()
    except:
       pass
    spd = speedtest.Speedtest()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await new_msg.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await new_msg.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await new_msg.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )

@Client.on_message(
    filters.command(["absen"], "") & filters.user(DEVS) & ~filters.me
)
async def absen(client: Client, message: Message):
    await message.reply(random.choice(kopi))

@Client.on_message(
    filters.command(["naya"], "") & filters.user(DEVS) & ~filters.me
)
async def naya(client, message):
    await message.reply("**Iya Naya Punya Nya Kynan**🤩")

@Client.on_message(
    filters.command("gping", [""]) & filters.user(DEVS) & ~filters.me
)
async def cpingme(client: Client, message: Message):
    """Ping the assistant"""
    mulai = time.time()
    akhir = time.time()
    await message.reply_text(
      f"**🏓 Pong!**\n`{round((akhir - mulai) * 1000)}ms`"
      )
      
@Client.on_message(
    filters.command(["cping"], "") & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command(["ping"], "") & filters.me)
async def pingme(client, message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ping_ = await client.send_message(client.me.id, "😈")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await message.reply_text(
        f"**Pong!**\n`%sms`\n" % (duration)
        )
    await ping_.delete()
  
  
@Client.on_message(filters.command(["setprefix", "sp"], cmds) & filters.me)
async def setprefix_(c: Client, m: Message):
    biji = get_arg(m)
    if not biji:
        sempak = await get_prefix()
        return await eor(
            m,
            f"Set your prefix using {cmds}setprefix [new_prefix]\n • Current prefix is {sempak}",
            time=10,
        )
    else:
        await set_prefix(biji)
        await m.edit(f"☑️ Prefix changed to [{biji}]")
        
        
@Client.on_message(filters.command(["pong"], cmds) & filters.me)
async def pongme(client, message):
    sempak = await get_prefix()
    if message.text.startswith(sempak+"pong"):
        uptime = await get_readable_time((time.time() - StartTime))
        start = datetime.now()
        ping_ = await client.send_message(client.me.id, "😈")
        end = datetime.now()
        duration = (end - start).microseconds / 1000
        await message.reply_text(
            f"**Pong!**\n`%sms`\n" % (duration)
        )
        await ping_.delete()