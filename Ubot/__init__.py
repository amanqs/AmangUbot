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


client1 = (
    Client(
        name="client1",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION1,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    clients.append(client1)
    if SESSION1
    else None
)

client2 = (
    Client(
        name="client2",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION2,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    clients.append(client2)
    if SESSION2
    else None
)

client3 = (
    Client(
        name="client3",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION3,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    clients.append(client3)
    if SESSION3
    else None
)

client4 = (
    Client(
        name="client4",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION4,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    clients.append(client4)
    if SESSION4
    else None
)

client5 = (
    Client(
        name="client5",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION5,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    clients.append(client5)
    if SESSION5
    else None
)
client6 = (
    Client(
        name="client6",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION6,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    clients.append(client6)
    if SESSION6
    else None
)

client7 = (
    Client(
        name="client7",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION7,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    clients.append(client7)
    if SESSION7
    else None
)

client8 = (
    Client(
        name="client8",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION8,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    clients.append(client8)
    if SESSION8
    else None
)

client9 = (
    Client(
        name="client9",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION9,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    clients.append(client9)
    if SESSION9
    else None
)

client10 = (
    Client(
        name="client10",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION10,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    clients.append(client10)
    if SESSION10
    else None
)

client11 = (
    Client(
        name="client11",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION11,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    clients.append(client11)
    if SESSION11
    else None
)

client12 = (
    Client(
        name="client12",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION12,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    clients.append(client12)
    if SESSION12
    else None
)

client13 = (
    Client(
        name="client13",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION13,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    clients.append(client13)
    if SESSION13
    else None
)

client14 = (
    Client(
        name="client14",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION14,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    clients.append(client14)
    if SESSION14
    else None
)

client15 = (
    Client(
        name="client15",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION15,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    clients.append(client15)
    if SESSION15
    else None
)

client16 = (
    Client(
        name="client16",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION16,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    clients.append(client16)
    if SESSION16
    else None
)

client17 = (
    Client(
        name="client17",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION17,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    clients.append(client17)
    if SESSION17
    else None
)

client18 = (
    Client(
        name="client18",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION18,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    clients.append(client18)
    if SESSION18
    else None
)

client19 = (
    Client(
        name="client19",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION19,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    clients.append(client19)
    if SESSION19
    else None
)

client20 = (
    Client(
        name="client20",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION20,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    clients.append(client20)
    if SESSION20
    else None
)
client21 = (
    Client(
        name="client21",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION21,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION21
    else None
)

client22 = (
    Client(
        name="client22",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION22,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION22
    else None
)

client23 = (
    Client(
        name="client23",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION23,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION23
    else None
)

client24 = (
    Client(
        name="client24",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION24,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION24
    else None
)

client25 = (
    Client(
        name="client25",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION25,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION25
    else None
)

client26 = (
    Client(
        name="client26",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION26,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION26
    else None
)

client27 = (
    Client(
        name="client27",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION27,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION27
    else None
)

client28 = (
    Client(
        name="client28",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION28,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION28
    else None
)

client29 = (
    Client(
        name="client29",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION29,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION29
    else None
)

client30 = (
    Client(
        name="client30",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION30,
        plugins=dict(root="Ubot/modules"),
        in_memory=True,
    )
    if SESSION30
    else None
)

  
clients = [client for client in [client1, client2, client3, client4, client5, client6, client7, client8, client9, client10, client11, client12, client13, client14, client15, client16, client17, client18, client19, client20, client21, client22, client23, client24, client25, client26, client27, client28, client29, client30] if client]

for client in clients:
    if not hasattr(client, "group_call"):
        setattr(client, "group_call", GroupCallFactory(client).get_group_call())
