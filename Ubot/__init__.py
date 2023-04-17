import asyncio
import logging
import sys
import time
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler
from typing import Any, Dict
from aiohttp import ClientSession
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from gpytranslate import Translator
from pyrogram import Client, filters, __version__, enums
from pytgcalls import GroupCallFactory
from ast import parse
from .logging import LOGGER
from config import *
cmds = [".", "^", "!", "?", ","]
CMD_HELP = {}
clients = []
ids = []


BOTLOG_CHATID = BOTLOG_CHATID or "me"
trl = Translator()
aiosession = ClientSession()
CMD_HELP = {}
scheduler = AsyncIOScheduler()
StartTime = time.time()
START_TIME = datetime.now()


LOOP = asyncio.get_event_loop_policy()
event_loop = LOOP.get_event_loop()
asyncio.set_event_loop(event_loop)


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="ubot",
            api_hash=API_HASH,
            api_id=API_ID,
            bot_token=BOT_TOKEN,
            workers=BOT_WORKERS,
            plugins=dict(root="Ubot/modules/bot"),
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = self.me
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} based on Pyrogram v{__version__} "
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Amang stopped. Bye.")


app = Bot()

if not BOT_TOKEN:
   LOGGER(__name__).error("WARNING: BOT TOKEN TIDAK DITEMUKAN, SHUTDOWN BOT")
   sys.exit()

bot1 = (
    Client(
        name="bot1",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION1,
        workers=USER_WORKERS,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION1
    else None
)

bot2 = (
    Client(
        name="bot2",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION2,
        workers=USER_WORKERS,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION2
    else None
)

bot3 = (
    Client(
        name="bot3",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION3,
        workers=USER_WORKERS,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION3
    else None
)

bot4 = (
    Client(
        name="bot4",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION4,
        workers=USER_WORKERS,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION4
    else None
)

bot5 = (
    Client(
        name="bot5",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION5,
        workers=USER_WORKERS,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION5
    else None
)
bot6 = (
    Client(
        name="bot6",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION6,
        workers=USER_WORKERS,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION6
    else None
)

bot7 = (
    Client(
        name="bot7",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION7,
        workers=USER_WORKERS,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION7
    else None
)

bot8 = (
    Client(
        name="bot8",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION8,
        workers=USER_WORKERS,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION8
    else None
)

bot9 = (
    Client(
        name="bot9",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION9,
        workers=USER_WORKERS,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION9
    else None
)

bot10 = (
    Client(
        name="bot10",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION10,
        workers=USER_WORKERS,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION10
    else None
)

bot11 = (
    Client(
        name="bot11",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION11,
        workers=USER_WORKERS,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION11
    else None
)

bot12 = (
    Client(
        name="bot12",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION12,
        workers=USER_WORKERS,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION12
    else None
)

bot13 = (
    Client(
        name="bot13",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION13,
        workers=USER_WORKERS,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION13
    else None
)

bot14 = (
    Client(
        name="bot14",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION14,
        workers=USER_WORKERS,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION14
    else None
)

bot15 = (
    Client(
        name="bot10",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION15,
        workers=USER_WORKERS,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION15
    else None
)
  
bots = [bot for bot in [bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9, bot10, bot11, bot12, bot13, bot14, bot15] if bot]

for bot in bots:
    if not hasattr(bot, "group_call"):
        setattr(bot, "group_call", GroupCallFactory(bot).get_group_call())
