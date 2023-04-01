import importlib
import time
from datetime import datetime
import asyncio
from pyrogram import idle
from pyrogram.errors import RPCError
from uvloop import install
from ubotlibs import *
from Ubot import aiosession, clients, app, ids, LOOP
from platform import python_version as py
from Ubot.logging import LOGGER
from pyrogram import __version__ as pyro
import sqlite3
from Ubot.modules import ALL_MODULES
from Ubot.core.db import *
from config import SUPPORT, CHANNEL
import os
from dotenv import load_dotenv
from pyrogram.errors import RPCError

BOT_VER ="8.1.0"


MSG_ON = """
**Naya Premium Actived ✅**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
◉ **Versi** : `{}`
◉ **Phython** : `{}`
◉ **Pyrogram** : `{}`
**Ketik** `alive` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


async def start_bot():
    await app.start()
    LOGGER("Naya Premium").info("Memulai Ubot Pyro..")
    for all_module in ALL_MODULES:
        importlib.import_module("Ubot.modules" + all_module)
    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            user_id = ex.id
            await buat_log(cli)
            botlog_chat_id = await get_botlog(user_id)
            LOGGER("Info").info("Startup Completed")
            LOGGER("√").info(f"Started as {ex.first_name}")
            ids.append(ex.id)
            await join(cli)
            await cli.send_message(botlog_chat_id, MSG_ON.format(BOT_VER, py(), pyro))
        except Exception as e:
            LOGGER("X").info(f"{e}")
    await idle()
    install()
    await aiosession.close()
    await app.stop()
    


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())

"""
if __name__ == "__main__":
    LOGGER("Naya Premium").info("Starting  Ubot")
    
    LOOP.run_until_complete(main())
"""
