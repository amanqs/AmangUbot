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


if SESSION1:
   print("Client1: Found.. Starting..📳")
   client1 = Client(name="client1", api_id=API_ID, api_hash=API_HASH, session_string=SESSION1, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   clients.append(client1)

if SESSION2:
   print("Client2: Found.. Starting.. 📳")
   client2 = Client(name="client2", api_id=API_ID, api_hash=API_HASH, session_string=SESSION2, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   clients.append(client2)

if SESSION3:
   print("Client3: Found.. Starting.. 📳")
   client3 = Client(name="client3", api_id=API_ID, api_hash=API_HASH, session_string=SESSION3, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   clients.append(client3)

if SESSION4:
   print("Client4: Found.. Starting.. 📳")
   client4 = Client(name="client4", api_id=API_ID, api_hash=API_HASH, session_string=SESSION4, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   clients.append(client4)

if SESSION5:
   print("Client5: Found.. Starting.. 📳")
   client5 = Client(name="client5", api_id=API_ID, api_hash=API_HASH, session_string=SESSION5, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   clients.append(client5)

if SESSION6:
   print("Client6: Found.. Starting.. 📳")
   client6 = Client(name="client6", api_id=API_ID, api_hash=API_HASH, session_string=SESSION6, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   clients.append(client6)

if SESSION7:
   print("Client7: Found.. Starting.. 📳")
   client7 = Client(name="client7", api_id=API_ID, api_hash=API_HASH, session_string=SESSION7, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   clients.append(client7)

if SESSION8:
   print("Client8: Found.. Starting.. 📳")
   client8 = Client(name="client8", api_id=API_ID, api_hash=API_HASH, session_string=SESSION8, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   clients.append(client8)

if SESSION9:
   print("Client9: Found.. Starting.. 📳")
   client9 = Client(name="client9", api_id=API_ID, api_hash=API_HASH, session_string=SESSION9, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   clients.append(client9)

if SESSION10:
   print("Client10: Found.. Starting.. 📳")
   client10 = Client(name="client10", api_id=API_ID, api_hash=API_HASH, session_string=SESSION10, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules")) 
   clients.append(client10)
   
if SESSION11:
   print("client11: Found.. Starting..📳")
   client11 = client1(name="client11", api_id=API_ID, api_hash=API_HASH, session_string=SESSION11, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   client1s.append(client11)

if SESSION12:
   print("client12: Found.. Starting.. 📳")
   client12 = client1(name="client12", api_id=API_ID, api_hash=API_HASH, session_string=SESSION12, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   client1s.append(client12)

if SESSION13:
   print("client13: Found.. Starting.. 📳")
   client13 = client1(name="client13", api_id=API_ID, api_hash=API_HASH, session_string=SESSION13, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   client1s.append(client13)

if SESSION14:
   print("client14: Found.. Starting.. 📳")
   client14 = client1(name="client14", api_id=API_ID, api_hash=API_HASH, session_string=SESSION14, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   client1s.append(client14)

if SESSION15:
   print("client15: Found.. Starting.. 📳")
   client15 = client1(name="client15", api_id=API_ID, api_hash=API_HASH, session_string=SESSION15, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   client1s.append(client15)

if SESSION16:
   print("client16: Found.. Starting.. 📳")
   client16 = client1(name="client16", api_id=API_ID, api_hash=API_HASH, session_string=SESSION16, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   client1s.append(client16)

if SESSION17:
   print("client17: Found.. Starting.. 📳")
   client17 = client1(name="client17", api_id=API_ID, api_hash=API_HASH, session_string=SESSION17, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   client1s.append(client17)

if SESSION18:
   print("client18: Found.. Starting.. 📳")
   client18 = client1(name="client18", api_id=API_ID, api_hash=API_HASH, session_string=SESSION18, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   client1s.append(client18)

if SESSION19:
   print("client19: Found.. Starting.. 📳")
   client19 = client1(name="client19", api_id=API_ID, api_hash=API_HASH, session_string=SESSION19, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   client1s.append(client19)

if SESSION20:
   print("client110: Found.. Starting.. 📳")
   client110 = client1(name="client110", api_id=API_ID, api_hash=API_HASH, session_string=SESSION20, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules")) 
   client1s.append(client20)
   
if SESSION21:
   print("client11: Found.. Starting..📳")
   client11 = client1(name="client11", api_id=API_ID, api_hash=API_HASH, session_string=SESSION21, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   client1s.append(client11)

if SESSION22:
   print("client12: Found.. Starting.. 📳")
   client12 = client1(name="client12", api_id=API_ID, api_hash=API_HASH, session_string=SESSION22, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   client1s.append(client12)

if SESSION23:
   print("client13: Found.. Starting.. 📳")
   client13 = client1(name="client13", api_id=API_ID, api_hash=API_HASH, session_string=SESSION23, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   client1s.append(client13)

if SESSION24:
   print("client14: Found.. Starting.. 📳")
   client14 = client1(name="client14", api_id=API_ID, api_hash=API_HASH, session_string=SESSION24, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   client1s.append(client14)

if SESSION25:
   print("client15: Found.. Starting.. 📳")
   client15 = client1(name="client15", api_id=API_ID, api_hash=API_HASH, session_string=SESSION25, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   client1s.append(client15)

if SESSION26:
   print("client16: Found.. Starting.. 📳")
   client16 = client1(name="client16", api_id=API_ID, api_hash=API_HASH, session_string=SESSION26, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   client1s.append(client16)

if SESSION27:
   print("client17: Found.. Starting.. 📳")
   client17 = client1(name="client17", api_id=API_ID, api_hash=API_HASH, session_string=SESSION27, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   client1s.append(client17)

if SESSION28:
   print("client18: Found.. Starting.. 📳")
   client18 = client1(name="client18", api_id=API_ID, api_hash=API_HASH, session_string=SESSION28, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   client1s.append(client18)

if SESSION20:
   print("client19: Found.. Starting.. 📳")
   client19 = client1(name="client29", api_id=API_ID, api_hash=API_HASH, session_string=SESSION29, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules"))
   client1s.append(client29)

if SESSION30:
   print("client110: Found.. Starting.. 📳")
   client110 = client1(name="client30", api_id=API_ID, api_hash=API_HASH, session_string=SESSION30, bot_token=BOT_TOKEN, plugins=dict(root="Ubot/modules")) 
   client1s.append(client30)
   
  
clients = [client for client in [client1, client2, client3, client4, client5, client6, client7, client8, client9, client10, client11, client12, client13, client14, client15, client16, client17, client18, client19, client20, client21, client22, client23, client24, client25, client26, client27, client28, client29, client30] if client]

for client in clients:
    if not hasattr(client, "group_call"):
        setattr(client, "group_call", GroupCallFactory(client).get_group_call())
