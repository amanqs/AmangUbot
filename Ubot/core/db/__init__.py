
from pyrogram.filters import chat
from pyrogram import Client, filters
from pyrogram.types import Message
from typing import Dict, List, Union
from datetime import datetime, timedelta
import pymongo.errors
from platform import python_version as py
from pyrogram import __version__ as pyro
from ubotlibs.ubot.utils import *
from Ubot.modules.basic import ADMINS
from dateutil.relativedelta import relativedelta
from ubotlibs.ubot.database import cli
import asyncio
import requests
import asyncio
from Ubot import *

from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from config import *


mongo = MongoCli(MONGO_URL)
db = mongo.ubot

coupledb = db.couple
notesdb = db.notes
filtersdb = db.filters
accesdb = db.acces
usersdb = db.users
logdb = db.gruplog
blchatdb = db.blchat
pmdb = db.pmpermit
afkdb = db.afk
prefdb = db.prefix
        

        
async def buat_log(bot):
    user = await bot.get_me()
    user_id = user.id
    user_data = await usersdb.users.find_one({"user_id": user_id})
    botlog_chat_id = None

    if user_data:
        botlog_chat_id = user_data.get("bot_log_group_id")

    if not user_data or not botlog_chat_id:
        group_name = 'Naya Premium Log'
        group_description = 'Jangan Hapus Atau Keluar Dari Grup Ini\n\nCreated By @NayaProjectBot.\nJika menemukan kendala atau ingin menanyakan sesuatu\nHubungi : @kenapanan, @rizzvbss atau bisa ke @KynanSupport.'
        group = await bot.create_supergroup(group_name, group_description)
        botlog_chat_id = group.id
        message_text = 'Grup Log Berhasil Dibuat,\nKetik `id` untuk mendapatkan id log grup\nKemudian ketik `setlog` ID_GROUP\n\nContoh : setlog -100749492984\n\n**Notes** : Ini adalah userbot tanpa prefix jadi tidak perlu memakai triger `.`'
        await bot.send_message(botlog_chat_id, message_text)
        await asyncio.sleep(1)
        
        await usersdb.users.update_one(
            {"user_id": user_id},
            {"$set": {"bot_log_group_id": botlog_chat_id}},
            upsert=True
        )
    
    if botlog_chat_id is None:
        return None
    
    return int(botlog_chat_id)



async def get_botlog(user_id: int):
    user_data = await logdb.users.find_one({"user_id": user_id})
    botlog_chat_id = user_data.get("bot_log_group_id") if user_data else None
    return botlog_chat_id

async def set_botlog(user_id: int, botlog_chat_id: int):
    await logdb.users.update_one(
        {"user_id": user_id},
        {"$set": {"bot_log_group_id": botlog_chat_id}},
        upsert=True
    )

async def get_log_groups(user_id: int):
    user_data = await logdb.users.find_one({"user_id": user_id})
    botlog_chat_id = user_data.get("bot_log_group_id") if user_data else []
    return botlog_chat_id



async def _get_lovers(chat_id: int):
    lovers = await coupledb.find_one({"chat_id": chat_id})
    if lovers:
        lovers = lovers["couple"]
    else:
        lovers = {}
    return lovers


async def get_couple(chat_id: int, date: str):
    lovers = await _get_lovers(chat_id)
    if date in lovers:
        return lovers[date]
    else:
        return False


async def save_couple(chat_id: int, date: str, couple: dict):
    lovers = await _get_lovers(chat_id)
    lovers[date] = couple
    await coupledb.update_one(
        {"chat_id": chat_id},
        {"$set": {"couple": lovers}},
        upsert=True,
    )


async def get_notes_count() -> dict:
    chats_count = 0
    notes_count = 0
    async for chat in notesdb.find({"user_id": {"$exists": 1}}):
        notes_name = await get_note_names(chat["user_id"])
        notes_count += len(notes_name)
        chats_count += 1
    return {"chats_count": chats_count, "notes_count": notes_count}


async def _get_notes(user_id: int) -> Dict[str, int]:
    _notes = await notesdb.find_one({"user_id": user_id})
    if not _notes:
        return {}
    return _notes["notes"]


async def get_note_names(user_id: int) -> List[str]:
    _notes = []
    for note in await _get_notes(user_id):
        _notes.append(note)
    return _notes


async def get_note(user_id: int, name: str) -> Union[bool, dict]:
    name = name.lower().strip()
    _notes = await _get_notes(user_id)
    if name in _notes:
        return _notes[name]
    return False


async def save_note(user_id: int, name: str, note: dict):
    name = name.lower().strip()
    _notes = await _get_notes(user_id)
    _notes[name] = note

    await notesdb.update_one(
        {"user_id": user_id}, {"$set": {"notes": _notes}}, upsert=True
    )


async def delete_note(user_id: int, name: str) -> bool:
    notesd = await _get_notes(user_id)
    name = name.lower().strip()
    if name in notesd:
        del notesd[name]
        await notesdb.update_one(
            {"user_id": user_id},
            {"$set": {"notes": notesd}},
            upsert=True,
        )
        return True
    return False


def obj_to_str(obj):
    if not obj:
        return False
    string = codecs.encode(pickle.dumps(obj), "base64").decode()
    return string


def str_to_obj(string: str):
    obj = pickle.loads(codecs.decode(string.encode(), "base64"))
    return obj

async def get_filters_count() -> dict:
    chats_count = 0
    filters_count = 0
    async for chat in filtersdb.find({"chat_id": {"$lt": 0}}):
        filters_name = await get_filters_names(chat["chat_id"])
        filters_count += len(filters_name)
        chats_count += 1
    return {
        "chats_count": chats_count,
        "filters_count": filters_count,
    }


async def _get_filters(user_id: int, chat_id: int) -> Dict[str, int]:
    _filters = await filtersdb.find_one({"user_id": user_id, "chat_id": chat_id})
    if not _filters:
        return {}
    return _filters["filters"]


async def get_filters_names(user_id: int, chat_id: int) -> List[str]:
    _filters = []
    for _filter in await _get_filters(user_id, chat_id):
        _filters.append(_filter)
    return _filters


async def get_filter(user_id: int, chat_id: int, name: str) -> Union[bool, dict]:
    name = name.lower().strip()
    _filters = await _get_filters(user_id, chat_id)
    if name in _filters:
        return _filters[name]
    return False



async def save_filter(user_id: int, chat_id: int, name: str, _filter: dict):
    name = name.lower().strip()
    _filters = await _get_filters(user_id, chat_id)
    _filters[name] = _filter
    await filtersdb.update_one(
    {"user_id": user_id, "chat_id": chat_id},
    {"$set": {"filters": _filters}},
    upsert=True
)



async def delete_filter(user_id: int, chat_id: int, name: str) -> bool:
    filtersd = await _get_filters(user_id, chat_id)
    name = name.lower().strip()
    if name in filtersd:
        del filtersd[name]
        await filtersdb.update_one(
            {"user_id": user_id, "chat_id": chat_id},
            {"$set": {"filters": filtersd}},
            upsert=True,
        )
        return True
    return False

        
async def blacklisted_chats(user_id: int) -> list:
    chats_list = []
    async for chat in blchatdb.users.find({"user_id": user_id, "chat_id": {"$lt": 0}}):
        chats_list.append(chat["chat_id"])
    return chats_list

async def blacklist_chat(user_id: int, chat_id: int) -> bool:
    if not await blchatdb.users.find_one({"user_id": user_id, "chat_id": chat_id}):
        await blchatdb.users.insert_one({"user_id": user_id, "chat_id": chat_id})
        return True
    return False


async def whitelist_chat(user_id: int, chat_id: int) -> bool:
    if await blchatdb.users.find_one({"user_id": user_id, "chat_id": chat_id}):
        await blchatdb.users.delete_one({"user_id": user_id, "chat_id": chat_id})
        return True
    return False


async def go_afk(user_id: int, time, reason=""):
    user_data = await afkdb.users.find_one({"user_id": user_id})
    if user_data:
        await afkdb.users.update_one({"user_id": user_id}, {"$set": {"afk": True, "time": time, "reason": reason}})
    else:
        await afkdb.users.insert_one({"user_id": user_id, "afk": True, "time": time, "reason": reason})


async def no_afk(user_id: int):
    await afkdb.users.delete_one({"user_id": user_id, "afk": True})


async def check_afk(user_id: int):
    user_data = await afkdb.users.find_one({"user_id": user_id, "afk": True})
    return user_data

sys:1: RuntimeWarning: coroutine 'nyet.<locals>.wrapper' was never awaited

async def get_prefix():
    prefix_config = await prefdb.find_one({"key": "prefix"})
    if prefix_config:
        return prefix_config["value"]
    else:
        return "."

async def set_prefix(new_prefix):
    await prefdb.update_one(
        {"key": "prefix"},
        {"$set": {"value": new_prefix}},
        upsert=True
    )
  
def nyet(command: str):
    async def wrapper(func):
        prefix = await get_prefix()
        @Client.on_message(filters.command(command, prefix) & filters.me)
        async def wrapped_func(client, message):
            await func(client, message)
        return wrapped_func
    return wrapper()


