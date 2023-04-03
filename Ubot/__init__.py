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



AI = OPENAI_API
PM_LOGGER = PM_LOGGER

if BOTLOG_CHATID:
   BOTLOG_CHATID = BOTLOG_CHATID
else:
   BOTLOG_CHATID = "me"

API_HASH = API_HASH
API_ID = API_ID
BOT_WORKERS = BOT_WORKERS



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
        self.LOGGER(__name__).info("Naya-Pyro stopped. Bye.")

app = Bot()


if SESSION1 is not None:
   client1 = Client(name="client1", api_id=API_ID, api_hash=API_HASH, session_string=SESSION1, plugins=dict(root="Ubot/modules"))
   clients.append(client1)

if SESSION2 is not None:
   client2 = Client(name="client2", api_id=API_ID, api_hash=API_HASH, session_string=SESSION2, plugins=dict(root="Ubot/modules"))
   clients.append(client2)

if SESSION3 is not None:
   client3 = Client(name="client3", api_id=API_ID, api_hash=API_HASH, session_string=SESSION3, plugins=dict(root="Ubot/modules"))
   clients.append(client3)

if SESSION4 is not None:
   client4 = Client(name="client4", api_id=API_ID, api_hash=API_HASH, session_string=SESSION4, plugins=dict(root="Ubot/modules"))
   clients.append(client4)

if SESSION5 is not None:
   client5 = Client(name="client5", api_id=API_ID, api_hash=API_HASH, session_string=SESSION5, plugins=dict(root="Ubot/modules"))
   clients.append(client5)

if SESSION6 is not None:
   client6 = Client(name="client6", api_id=API_ID, api_hash=API_HASH, session_string=SESSION6, plugins=dict(root="Ubot/modules"))
   clients.append(client6)

if SESSION7 is not None:
   client7 = Client(name="client7", api_id=API_ID, api_hash=API_HASH, session_string=SESSION7, plugins=dict(root="Ubot/modules"))
   clients.append(client7)

if SESSION8 is not None:
   client8 = Client(name="client8", api_id=API_ID, api_hash=API_HASH, session_string=SESSION8, plugins=dict(root="Ubot/modules"))
   clients.append(client8)

if SESSION9 is not None:
   client9 = Client(name="client9", api_id=API_ID, api_hash=API_HASH, session_string=SESSION9, plugins=dict(root="Ubot/modules"))
   clients.append(client9)

if SESSION10 is not None:
   client10 = Client(name="client10", api_id=API_ID, api_hash=API_HASH, session_string=SESSION10, plugins=dict(root="Ubot/modules")) 
   clients.append(client10)
   
  
clients = [client for client in [client1, client2, client3, client4, client5, client6, client7, client8, client9, client10] if client]

for client in clients:
    if not hasattr(client, "group_call"):
        setattr(client, "group_call", GroupCallFactory(client).get_group_call())