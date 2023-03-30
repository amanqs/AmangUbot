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
cmds = None
CMD_HELP = {}
clients = []
ids = []

SUDOERS = filters.user()
SUDO_USER = SUDOERS

AI = OPENAI_API
PM_LOGGER = PM_LOGGER

if BOTLOG_CHATID:
   BOTLOG_CHATID = BOTLOG_CHATID
else:
   BOTLOG_CHATID = "me"

BOT_WORKERS = BOT_WORKERS
API_HASH = API_HASH
API_ID = API_ID
BOT_WORKERS = BOT_WORKERS


SUDO_USER = SUDOERS
trl = Translator()
aiosession = ClientSession()
CMD_HELP = {}
scheduler = AsyncIOScheduler()
StartTime = time.time()
START_TIME = datetime.now()
TEMP_SETTINGS: Dict[Any, Any] = {}
TEMP_SETTINGS["PM_COUNT"] = {}
TEMP_SETTINGS["PM_LAST_MSG"] = {}

LOOP = asyncio.get_event_loop()




class Bot(Client):
    def __init__(self):
        super().__init__(
            name="ubot",
            api_hash=API_HASH,
            api_id=API_ID,
            bot_token=BOT_TOKEN,
            plugins=dict(root="Ubot/modules/bot"),
            workers=BOT_WORKERS,
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
        self.LOGGER(__name__).info("SessionMakerBot stopped. Bye.")

app = Bot()


bot1 = (
    Client(
        name="bot1",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION1,
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
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION4
    else None
)

bot15 = (
    Client(
        name="bot15",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION15,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION15
    else None
)

bot16 = (
    Client(
        name="bot16",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION16,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION16
    else None
)

bot17 = (
    Client(
        name="bot17",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION17,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION17
    else None
)

bot18 = (
    Client(
        name="bot18",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION18,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION18
    else None
)

bot19 = (
    Client(
        name="bot19",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION19,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION19
    else None
)

bot20 = (
    Client(
        name="bot20",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION20,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION20
    else None
)
bot21 = (
    Client(
        name="bot21",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION21,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION21
    else None
)

bot22 = (
    Client(
        name="bot22",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION22,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION22
    else None
)

bot23 = (
    Client(
        name="bot23",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION23,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION23
    else None
)

bot24 = (
    Client(
        name="bot24",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION24,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION24
    else None
)

bot25 = (
    Client(
        name="bot25",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION25,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION25
    else None
)

bot26 = (
    Client(
        name="bot26",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION26,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION26
    else None
)

bot27 = (
    Client(
        name="bot27",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION27,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION27
    else None
)

bot28 = (
    Client(
        name="bot28",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION28,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION28
    else None
)

bot29 = (
    Client(
        name="bot29",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION29,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION29
    else None
)

bot30 = (
    Client(
        name="bot30",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION30,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION30
    else None
)


bots = [bot for bot in [bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9, bot10, bot11, bot12, bot13, bot14, bot15, bot16, bot17, bot18, bot19, bot20, bot21, bot22, bot23, bot24, bot25, bot26, bot27, bot28, bot29, bot30] if bot]

for bot in bots:
    if not hasattr(bot, "group_call"):
        setattr(bot, "group_call", GroupCallFactory(bot).get_group_call())
