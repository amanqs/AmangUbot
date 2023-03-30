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
from pyrogram import Client, filters
from pytgcalls import GroupCallFactory
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
    """ modded client for SessionMakerBot """

    def __init__(self):
        super().__init__(
            name="ubot",
            api_hash=API_HASH,
            api_id=API_ID,
            bot_token=BOT_TOKEN,
            plugins={
                "root": "Ubot/modules/bot"
            },
            workers=BOT_WORKERS,
        )
#        if not BOT_TOKEN:
        self.LOGGER = LOGGER
 #       else:
#            LOGGER(__name__).error("WARNING: BOT TOKEN TIDAK DITEMUKAN, SHUTDOWN BOT")
#            sys.exit()

    async def start(self):
        await super().start()
        usr_bot_me = self.me
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} based on Pyrogram v{__version__} "
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("SessionMakerBot stopped. Bye.")
        
class User1(Client):
    def __init__(self):
        super().__init__(
            name="bot1",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION1,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION1:
            self.LOGGER = LOGGER
        else:
            LOGGER(__name__).warning("STRING SESSION TIDAK DITEMUKAN, SHUTDOWN BOT!")
            sys.exit()

class User2(Client):
    def __init__(self):
        super().__init__(
            name="bot2",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION2,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION2:
            self.LOGGER = LOGGER
        else:
            LOGGER(__name__).warning("STRING SESSION TIDAK DITEMUKAN, SHUTDOWN BOT!")
            sys.exit()

class User3(Client):
    def __init__(self):
        super().__init__(
            name="bot3",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION3,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION3:
            self.LOGGER = LOGGER
        else:
            LOGGER(__name__).warning("STRING SESSION TIDAK DITEMUKAN, SHUTDOWN BOT!")
            sys.exit()

class User4(Client):
    def __init__(self):
        super().__init__(
            name="bot4",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION4,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION4:
            self.LOGGER = LOGGER
        else:
            None

class User5(Client):
    def __init__(self):
        super().__init__(
            name="bot5",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION5,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION5:
            self.LOGGER = LOGGER
        else:
            None

class User6(Client):
    def __init__(self):
        super().__init__(
            name="bot6",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION6,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION6:
            self.LOGGER = LOGGER
        else:
            None

class User7(Client):
    def __init__(self):
        super().__init__(
            name="bot7",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION7,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION7:
            self.LOGGER = LOGGER
        else:
            None

class User8(Client):
    def __init__(self):
        super().__init__(
            name="bot8",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION8,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION8:
            self.LOGGER = LOGGER
        else:
            None

class User9(Client):
    def __init__(self):
        super().__init__(
            name="bot9",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION9,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION9:
            self.LOGGER = LOGGER
        else:
            None

class User10(Client):
    def __init__(self):
        super().__init__(
            name="bot10",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION10,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION10:
            self.LOGGER = LOGGER
        else:
            None

    async def start(self):
        await super().start()
        usr_bot_me = self.me
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} based on Pyrogram v{__version__} "
        )
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")

app = Bot()

bot1 = User1()
bot2 = User2()
bot3 = User3()
bot4 = User4()
bot5 = User5()
bot6 = User6()
bot7 = User7()
bot8 = User8()
bot9 = User9()
bot10 = User10()




bots = [bot for bot in [bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9, bot10] if bot]

for bot in bots:
    if not hasattr(bot, "group_call"):
        setattr(bot, "group_call", GroupCallFactory(bot).get_group_call())
