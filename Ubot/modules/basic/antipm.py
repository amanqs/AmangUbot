# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


from .apm import get_arg
from pyrogram import filters, Client
from pyrogram.types import Message
from . import *
from Ubot.core.db.pmpermit import pm_guard
from Ubot.core.db import pmpermit as set

@Ubot("antipm", cmds)
async def pm_permit(client, message):
    arg = get_arg(message)
    user_id = client.me.id
    if not arg:
        await message.reply("**Gunakan format**:\n `antipm` on atau off")
        return
    if arg == "off":
        await set.set_pm(user_id, False)
        await message.edit("**AntiPM Dimatikan**")
    elif arg == "on":
        await set.set_pm(user_id, True)
        await message.edit("**AntiPM Diaktifkan**")
    else:
        await message.edit("**Gunakan format**:\n `antipm` on atau off")
    apaan = await pm_guard(user_id)
    if apaan:
        await message.edit("**AntiPM Dalam Keadaaan Hidup**")
    else:
        await message.edit("**AntiPM Dalam Keadaan Mati**")

        
@Ubot("setmsg", cmds)
async def setpmmsg(client, message):
    arg = get_arg(message)
    user_id = client.me.id
    if not arg:
        await message.reply("**Berikan pesan untuk mengatur**\nContoh : `setpm` `Hai apa ada yang bisa saya bantu ?`")
        return
    if arg == "default":
        await set.set_permit_message(user_id, set.PMPERMIT_MESSAGE)
        await message.edit("**Pesan AntiPM Diatur ke Default**.")
        return
    await set.set_permit_message(user_id, f"`{arg}`")
    await message.edit("**Berhasil mengatur pesan AntiPM**")


add_command_help(
    "antipm",
    [
        [f"antipm [on or off]", "Hidupkan dan matikan anti-pm."],
        [f"setmsg [text or default]", " -> Sets a custom anti-pm message."],
        [f"blockmsg [message or default]", "Setel pesan blokir."],
        [f"setlimit [angka]", "Peringatan pesan!."],
        [f"ok", "Setujui."],
        [f"no", "Tolak."],
    ],
)
