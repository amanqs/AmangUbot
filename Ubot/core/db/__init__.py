
from pyrogram.filters import chat
from pyrogram import Client
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
import codecs
import pickle
import math
import os
import dotenv
import heroku3
import requests
import urllib3
import schedule
import asyncio
from Ubot import *

from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from config import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(HEROKU_API_KEY),
    "https",
    str(HEROKU_APP_NAME),
    "HEAD",
    "main",
]

mongo = MongoCli(MONGO_URL)
db = mongo.ubot

coupledb = db.couple
karmadb = db.karma
notesdb = db.notes
filtersdb = db.filters
accesdb = db.acces
usersdb = db.users
logdb = db.gruplog
blchatdb = db.blchat
pmdb = db.pmpermit
gbansdb = db.gban
afkdb = db.afk

BOT_VER ="8.1.0"

MSG_ON = """
**New Ubot Actived ✅**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
◉ **Versi** : `{}`
◉ **Phython** : `{}`
◉ **Pyrogram** : `{}`
**Ketik** `alive` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""
        
        
        
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


async def grant_access(user_id: int) -> bool:
    access = {"user_id": user_id}
    try:
        result = await accesdb.users.update_one(
            {'user_id': user_id},
            {'$set': {'user_id': user_id}},
            upsert=True
        )
        if result.upserted_id or result.modified_count:
            return True
        else:
            return False
    except pymongo.errors.PyMongoError:
        return False
        

async def get_users_access() -> List[str]:
    try:
        cursor = accesdb.users.find({}, {'access_list': 1})
        users_access = set()
        async for document in cursor:
            if 'access_list' in document:
                users_access.update(document['access_list'])
        return list(users_access)
    except pymongo.errors.PyMongoError:
        return []


async def revoke_access(user_id: int) -> bool:
    try:
        user = await accesdb.users.find_one({'user_id': user_id})
        if user is not None and user.get('banned'):
            return False
        result = await accesdb.users.update_one(
            {'user_id': user_id},
            {'$set': {'banned': True}},
            upsert=True
        )
        if result.upserted_id:
            return False
        elif result.matched_count > 0 or result.modified_count > 0:
            return True
        else:
            return False
    except pymongo.errors.PyMongoError:
        return False


async def check_user_access(user_id: int) -> bool:
    access = {"user_id": user_id}
    result = await accesdb.users.find_one(access)
    if result:
        return True
    else:
        return False
        
async def delete_user_access(user_id: int) -> bool:
    try:
        result = await accesdb.users.delete_one({'user_id': user_id})
        if result.deleted_count > 0:
            return True
        else:
            return False
    except pymongo.errors.PyMongoError:
        return False

def check_access(func):
    async def wrapper(client, message):
        user_id = message.from_user.id
        user_access = await check_user_access(user_id)
        if user_id not in ADMINS and not user_access:
            await message.reply_text("Maaf, Anda tidak memiliki akses untuk menggunakan bot ini.\n Silakan ke @kynansupport untuk mendapatkan akses dari Admin disana.")
            return
        await func(client, message)
    return wrapper

async def get_expired_date(user_id):
    user = await accesdb.users.find_one({"_id": user_id})
    if user:
        expire_date = user.get("expire_date")
        if expire_date:
            remaining_days = (expire_date - datetime.now()).days
            remaining_days = (datetime.now() + timedelta(days=remaining_days)).strftime('%d-%m-%Y')
            return remaining_days
        else:
            return None
    else:
        return None


async def rem_expired_date(user_id):
    await accesdb.users.update_one(
        {"_id": user_id}, {"$unset": {"expire_date": ""}}, upsert=True
    )

async def remove_expired():
    async for user in accesdb.users.find({"expire_date": {"$lt": datetime.now()}}):
        await delete_user_access(user["_id"])
        await rem_expired_date(user["_id"])


async def set_expired_date(user_id, duration):
    days_in_month = 30
    if duration <= 12:
        days_in_month = 30 * duration
    expire_date = datetime.now() + timedelta(days=days_in_month)
    accesdb.users.update_one({"_id": user_id}, {"$set": {"expire_date": expire_date}}, upsert=True)
    schedule.every().day.at("00:00").do(remove_expired)
    asyncio.create_task(schedule_loop())



async def schedule_loop():
    while True:
        await asyncio.sleep(1)
        schedule.run_pending()

async def check_and_grant_user_access(user_id: int, duration: int) -> None:
    if await check_user_access(user_id):
        await delete_user_access(user_id)
    if await grant_access(user_id) and await set_expired_date(user_id, duration):
        return


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


async def get_karmas_count() -> dict:
    chats_count = 0
    karmas_count = 0
    async for chat in karmadb.find({"chat_id": {"$lt": 0}}):
        for i in chat["karma"]:
            karma_ = chat["karma"][i]["karma"]
            if karma_ > 0:
                karmas_count += karma_
        chats_count += 1
    return {"chats_count": chats_count, "karmas_count": karmas_count}


async def user_global_karma(user_id) -> int:
    total_karma = 0
    async for chat in karmadb.find({"chat_id": {"$lt": 0}}):
        karma = await get_karma(chat["chat_id"], await int_to_alpha(user_id))
        if karma and (int(karma["karma"]) > 0):
            total_karma += int(karma["karma"])
    return total_karma


async def get_karmas(chat_id: int) -> Dict[str, int]:
    karma = await karmadb.find_one({"chat_id": chat_id})
    if not karma:
        return {}
    return karma["karma"]


async def get_karma(chat_id: int, name: str) -> Union[bool, dict]:
    name = name.lower().strip()
    karmas = await get_karmas(chat_id)
    if name in karmas:
        return karmas[name]


async def update_karma(chat_id: int, name: str, karma: dict):
    name = name.lower().strip()
    karmas = await get_karmas(chat_id)
    karmas[name] = karma
    await karmadb.update_one(
        {"chat_id": chat_id}, {"$set": {"karma": karmas}}, upsert=True
    )


async def is_karma_on(chat_id: int) -> bool:
    chat = await karmadb.find_one({"chat_id_toggle": chat_id})
    if not chat:
        return True
    return False


async def karma_on(chat_id: int):
    is_karma = await is_karma_on(chat_id)
    if is_karma:
        return
    return await karmadb.delete_one({"chat_id_toggle": chat_id})


async def karma_off(chat_id: int):
    is_karma = await is_karma_on(chat_id)
    if not is_karma:
        return
    return await karmadb.insert_one({"chat_id_toggle": chat_id})


async def int_to_alpha(user_id: int) -> str:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    text = ""
    user_id = str(user_id)
    for i in user_id:
        text += alphabet[int(i)]
    return text


async def alpha_to_int(user_id_alphabet: str) -> int:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    user_id = ""
    for i in user_id_alphabet:
        index = alphabet.index(i)
        user_id += str(index)
    user_id = int(user_id)
    return user_id

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


async def send_tagalert_notification(client, user_id: int, status: bool):
    message = "Tag alert has been activated." if status else "Tag alert has been deactivated."
    await client.send_message(user_id, message)

async def update_tagalert_status(client, user_id: int, status: bool):
    user_data = await tagdb.find_one({"user_id": user_id})
    if user_data:
        tagdb.update_one({"user_id": user_id}, {"$set": {"tagalert_enabled": status}})
    else:
        tagdb.insert_one({"user_id": user_id, "tagalert_enabled": status})
    await send_tagalert_notification(client, user_id, status)


async def get_tagalert_status(user_id: int):
    user_data = await tagdb.find_one({"user_id": user_id})
    if user_data:
        return user_data.get("tagalert_enabled")
    else:
        return True
        

        
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
    
    
async def get_gbanned(user_id: int) -> list:
    results = []
    async for user in gbansdb.users.find({"user_id": user_id, "user_id": {"$gt": 0}}):
        user_id = user["user_id"]
        results.append(user_id)
    return results


async def is_gbanned_user(user_id: int) -> bool:
    user = await gbansdb.users.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def add_gban_user(user_id: int):
    is_gbanned = await is_gbanned_user(user_id)
    if is_gbanned:
        return
    return await gbansdb.users.insert_one({"user_id": user_id})


async def remove_gban_user(user_id: int):
    is_gbanned = await is_gbanned_user(user_id)
    if not is_gbanned:
        return
    return await gbansdb.users.delete_one({"user_id": user_id})


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

"""
async def go_afk(user_id: int, time, reason=""):
    midhun = await afkdb.users.find_one({"user_id": user_id, "user_id": "AFK"})
    if midhun:
        await afkdb.users.update_one({"user_id": user_id, "user_id": "AFK"}, {"$set": {"time": time, "reason": reason}})
    else:
        await afkdb.users.insert_one({"user_id": user_id, "user_id": "AFK", "time": time, "reason": reason})


async def no_afk(user_id: int):
    midhun = await afkdb.users.find_one({"user_id": user_id, "user_id": "AFK"})
    if midhun:
        await afkdb.users.delete_one({"user_id": user_id, "user_id": "AFK"})


async def check_afk(user_id: int):
    midhun = await afkdb.users.find_one({"user_id": user_id, "user_id": "AFK"})
    if midhun:
        return midhun
    else:
        return None
"""