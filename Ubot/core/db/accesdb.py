from pyrogram.filters import chat
from pyrogram import Client
from . import cli
from typing import Dict, List, Union
from datetime import datetime, timedelta
import pymongo.errors
from Ubot.modules.basic import ADMINS
from dateutil.relativedelta import relativedelta


import schedule
import asyncio


collection = cli["access"]


async def grant_access(user_id: int) -> bool:
    access = {"user_id": user_id}
    try:
        result = await collection.users.update_one(
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
        cursor = collection.users.find({}, {'access_list': 1})
        users_access = set()
        async for document in cursor:
            if 'access_list' in document:
                users_access.update(document['access_list'])
        return list(users_access)
    except pymongo.errors.PyMongoError:
        return []


async def revoke_access(user_id: int) -> bool:
    try:
        user = await collection.users.find_one({'user_id': user_id})
        if user is not None and user.get('banned'):
            return False
        result = await collection.users.update_one(
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
    result = await collection.users.find_one(access)
    if result:
        return True
    else:
        return False
        
async def delete_user_access(user_id: int) -> bool:
    try:
        result = await collection.users.delete_one({'user_id': user_id})
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
            await message.reply_text("This feature is only available for premium users.")
            return
        await func(client, message)
    return wrapper

async def get_expired_date(user_id):
    user = await collection.users.find_one({"_id": user_id})
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
    await collection.users.update_one(
        {"_id": user_id}, {"$unset": {"expire_date": ""}}, upsert=True
    )

async def remove_expired():
    async for user in collection.users.find({"expire_date": {"$lt": datetime.now()}}):
        await delete_user_access(user["_id"])
        await rem_expired_date(user["_id"])


async def set_expired_date(user_id, duration):
    days_in_month = 30
    if duration <= 12:
        days_in_month = 30 * duration
    expire_date = datetime.now() + timedelta(days=days_in_month)
    collection.users.update_one({"_id": user_id}, {"$set": {"expire_date": expire_date}}, upsert=True)
    schedule.every().day.at("00:00").do(remove_expired)
    asyncio.create_task(schedule_loop())

    
async def set_expired_days(user_id, duration):
    days_in_days = 1
    if duration <= 30:
        days_in_days = 1 * duration
    expire_date = datetime.now() + timedelta(days=days_in_days)
    collection.users.update_one({"_id": user_id}, {"$set": {"expire_date": expire_date}}, upsert=True)
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
