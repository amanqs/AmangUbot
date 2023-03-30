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
from ast import parse
from .bot import Bot
from .user import *
from .logging import LOGGER
from config import *
from Ubot.bot import Bot
from Ubot.user import *
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
bot11 = User11()
bot12 = User12()
bot13 = User13()
bot14 = User14()
bot15 = User15()
bot16 = User16()
bot17 = User17()
bot18 = User18()
bot19 = User19()
bot20 = User20()
bot21 = User21()
bot22 = User22()
bot23 = User23()
bot24 = User24()
bot25 = User25()
bot26 = User26()
bot27 = User27()
bot28 = User28()
bot29 = User29()
bot30 = User30()


bots = [bot for bot in [bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9, bot10, bot11, bot12, bot13, bot14, bot15, bot16, bot17, bot18, bot19, bot20, bot21, bot22, bot23, bot24, bot25, bot26, bot27, bot28, bot29, bot30] if bot]

for bot in bots:
    if not hasattr(bot, "group_call"):
        setattr(bot, "group_call", GroupCallFactory(bot).get_group_call())
