# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


from pyrogram import Client, filters
from pyrogram.types import Message
from . import *
import requests

@Ubot("nulis", cmds)
async def handwrite(client, message):
    if message.reply_to_message:
        naya = message.reply_to_message.text
    else:
        naya = message.text.split(None, 1)[1]
    nan = await message.reply("`Processing...`")
    ajg = requests.get(f"https://api.sdbots.tk/write?text={naya}").url
    await message.reply_photo(
        photo=ajg,
        caption=f"**Ditulis Oleh :** {client.me.mention}")
    await nan.delete()


add_command_help(
    "nulis",
    [
        [f"nulis [berikan pesan/balas ke pesan]", "Membuat Tulisan Untuk Kamu Yang Malas Nulis."],
    ],
)
