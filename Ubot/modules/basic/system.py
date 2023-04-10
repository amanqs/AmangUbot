
import sys
from os import environ, execle, remove

from pyrogram import Client, filters
from pyrogram.types import Message
from . import *
from Ubot.core.db import *
from config import *

HAPP = None

@Ubot("shutdown", cmds)
async def shutdown_bot(client, message):
    botlog_chat_id = await get_log_groups(user_id)
    if not botlog_chat_id:
        return await message.reply("`Maaf, tidak dapat menemukan ID chat log bot.`\nPastikan Anda Telah Mengtur Log Group Anda")
    await client.send_message(
            botlog_chat_id,
            "**#SHUTDOWN** \n"
            "**AmangUbot** telah di matikan!\nJika ingin menghidupkan kembali silahkan buka heroku",
        )
    await message.reply(" **AmangUbot Berhasil di matikan!**")
    if HAPP is not None:
        HAPP.process_formation()["worker"].scale(0)
    else:
        sys.exit(0)


@Ubot("logs", cmds)
async def logs_ubot(client, message):
    if HAPP is None:
        return await message.reply("Pastikan `HEROKU_API_KEY` dan `HEROKU_APP_NAME` anda dikonfigurasi dengan benar di config vars heroku",
        )
    biji = await message.reply("🧾 `Get Logs your Bots...`")
    with open("Logs-Heroku.txt", "w") as log:
        log.write(HAPP.get_log())
    await client.send_document(
        message.chat.id,
        "Logs-Heroku.txt",
        thumb="https://telegra.ph//file/976ad753d6073dde1f579.jpg",
        caption="**This is your Heroku Logs**",
    )
    await biji.delete()
    remove("Logs-Heroku.txt")
