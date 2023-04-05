
import random
import time
import traceback
from sys import version as pyver
from datetime import datetime
import os
import shlex
import textwrap
import asyncio 
from gc import get_objects

from pyrogram import __version__ as pyrover
from pyrogram.enums import ParseMode
from pyrogram import *
from pyrogram.types import *
from Ubot.core import *
from pyrogram.raw.functions import Ping
from Ubot import CMD_HELP, StartTime, app, ids, cmds
from config import OWNER_ID

BOT_VER = "5.0.0"

WHITE = [1970636001, 902478883, 2067434944, 1947740506, 1897354060, 1694909518, 5077932806]

BLACK = [1889573907, 1054295664, 1898065191]


def support():
    buttons = [
        [
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/kynansupport"),
        ],
        [
            InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="close"),
        ],
    ]
    return buttons

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time
    

async def alive_function(message, answers):
    users = 0
    group = 0
    async for dialog in message._client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE:
            users += 1
        elif dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            group += 1
    if message._client.me.id in BLACK:
        status = "OWNER"
    elif message._client.me.id is OWNER_ID:
        status = "ADMINS"
    else:
        status = "ADMINS"
    start = datetime.now()
    buttons = support()
    ex = await message._client.get_me()
    user = len(ids)
    remaining_days = "None"
    await message._client.invoke(Ping(ping_id=0))
    ping = (datetime.now() - start).microseconds / 1000
    uptime = await get_readable_time((time.time() - StartTime))
    msg = (
        f"<b>Naya-Premium</b>\n"
        f"    <b> status : {status} </b>\n"
        f"    <b> users :</b> <code>{user}</code>\n"
        f"    <b> ping_dc :</b> <code>{ping} ms</code>\n"
        f"    <b> users_count :</b> <code>{users} users</code>\n"
        f"    <b> groups_count :</b> <code>{group} group</code>\n"
        f"    <b> expired :</b> <i>{remaining_days}</i>\n"
        f"    <b> uptime :</b> <code>{uptime}</code>\n")
    answers.append(
        InlineQueryResultArticle(
            title="alive",
            input_message_content=InputTextMessageContent(
                msg, parse_mode=ParseMode.HTML, disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(buttons)))
    return answers



async def help_function(answers):
    bttn = paginate_help(0, CMD_HELP, "helpme")
    answers.append(
        InlineQueryResultArticle(
            title="Help Article!",
            input_message_content=InputTextMessageContent(
                Data.text_help_menu.format(len(CMD_HELP))
            ),
            reply_markup=InlineKeyboardMarkup(bttn),
        )
    )
    return answers


@app.on_inline_query()
# @inline_wrapper
async def inline_query_handler(client: Client, query):
    try:
        text = query.query.strip().lower()
        string_given = query.query.lower()
        answers = []
        answerss = []
        if text.strip() == "":
            return
        elif text.split()[0] == "alive":
            m = [obj for obj in get_objects() if id(obj) == int(query.query.split(None, 1)[1])][0]
            answerss = await alive_function(m, answers)
            await client.answer_inline_query(query.id, results=answerss, cache_time=10)
        elif string_given.startswith("helper"):
            answers = await help_function(answers)
            await client.answer_inline_query(query.id, results=answers, cache_time=0)

    except Exception as e:
        e = traceback.format_exc()
        print(e, "InLine")
      
