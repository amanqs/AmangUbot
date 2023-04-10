# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

# Credits by : https://t.me/xtsea

import os
import requests
import random
import json
import asyncio
from pyrogram import Client, filters
from pyrogram.types import *

from . import * 

# isi var sini

API_KEY_GOOGLE = "AIzaSyDw5Ex6fufy_wGzSp20OkXODYh_bhuLPb0"
SEARCH_ENGINE_ID = "414b4c079845641a3" 

search_params = {
    'q': '',
    'num': 1,
    'imgSize': 'large',
    'imgType': 'photo',
    'searchType': 'image'
}

@Ubot(["gimg"], cmds)
async def api_google_image(c: Client, m: Message):
    if len(m.command) == 1:
       await m.reply_text(f"Example: `{m.command[0]} pocong`\n\n**Untuk pencarian khusus gambar google lainnya**")
       return

    search_term = m.text.split(" ", 1)[1]
    api_key = API_KEY_GOOGLE
    search_engine_id = SEARCH_ENGINE_ID
    if not api_key and not search_engine_id:
       await m.reply_text("Missing api key : `API_KEY_GOOGLE` and `SEARCH_ENGINE_ID`")
       return

    search_params['q'] = search_term
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}'
    response = requests.get(url, params=search_params)
    response_json = response.json()

    if "items" in response_json and len(response_json['items']) > 0:
        image_url = response_json['items'][0]['link']
        wtf = await m.reply_text("Uploading....")
        await asyncio.sleep(2)
        google_caption = f"**Powered By** {c.me.mention}"
        await c.send_photo(m.chat.id, image_url, caption=google_caption, reply_to_message_id=m.id)
    else:
        await wtf.edit_text("No results found for your search query.")
    try:
        await wtf.delete()
    except Exception:
        pass


add_command_help(
    "google",[
        [f"gimg <query>", "Membuat mencari gambar menggunakan Google."],
    ],
)