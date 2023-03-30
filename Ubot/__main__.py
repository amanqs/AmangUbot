import importlib
import time
from datetime import datetime
import asyncio
from pyrogram import idle

from uvloop import install
from ubotlibs import *
from Ubot import aiosession, bots, app, LOOP
from platform import python_version as py
from Ubot.logging import LOGGER
from pyrogram import __version__ as pyro
from Ubot.core.db import *

from Ubot.modules import ALL_MODULES
from config import SUPPORT, CHANNEL
import os
from dotenv import load_dotenv

CMD_HELP = {}
clients = []
ids = []

MSG_ON = """
**Naya Premium Actived ✅**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
◉ **Versi** : `{}`
◉ **Phython** : `{}`
◉ **Pyrogram** : `{}`
**Ketik** `alive`
**untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


async def main():
    await app.start()
    LOGGER("Naya Premium").info("Memulai..")
    for all_module in ALL_MODULES:
        importlib.import_module("Ubot.modules" + all_module)
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            user_id = ex.id
            await buat_log(bot)
            botlog_chat_id = await get_botlog(user_id)
            LOGGER("Log").info("Startup Completed")
            LOGGER("√").info(f"Started as {ex.first_name} | {ex.id} ")
            await join(bot)
            await bot.send_message(botlog_chat_id, MSG_ON.format(BOT_VER, py(), pyro))
            ids.append(ex.id)
        except Exception as e:
            LOGGER("X").info(f"{e}")
    await idle()
    await aiosession.close()
    


              

if __name__ == "__main__":
    LOGGER("Naya Premium").info("Starting Ubot")
    install()
    LOOP.run_until_complete(main())