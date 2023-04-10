
from io import BytesIO
from pyrogram import *
from pyrogram.types import *


from .carbon import make_carbon
from . import *



@Ubot("neofetch", cmds)
async def neofetch(client: Client, message: Message):
    chat_id = message.chat.id
    noob = await message.reply_text("`Prossing.....`")
    try:
        neofetch = (await shell_exec("neofetch --stdout"))[0]
        carbon = await make_carbon(neofetch)
        await noob.edit("`Uploading....`")
        await client.send_photo(chat_id, carbon, caption=f"**Carbonised by** {client.me.mention}")
        await noob.delete()
    except Exception:
        pass 

# you can add modules

# this code
