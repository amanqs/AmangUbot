# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import asyncio
from threading import Event

from pyrogram import Client, enums, filters
from pyrogram.types import Message
from ubotlibs.ubot.helper.basic import edit_or_reply
from ubotlibs.ubot.utils.misc import extract_args
from . import *


SPAM_COUNT = [0]

commands = ["spam", "statspam", "slowspam", "fspam"]

def increment_spam_count():
    SPAM_COUNT[0] += 1
    return spam_allowed()


def spam_allowed():
    return SPAM_COUNT[0] < 1000


@Ubot(["dspam"], cmds)
async def delayspam(client: Client, message: Message):

    delayspam = await extract_args(message)
    arr = delayspam.split()
    if len(arr) < 3 or not arr[0].isdigit() or not arr[1].isdigit():
        await message.edit("`Something seems missing / wrong.`")
        return
    delay = int(arr[0])
    count = int(arr[1])
    spam_message = delayspam.replace(arr[0], cmds, 1)
    spam_message = spam_message.replace(arr[1], cmds, 1).strip()
    await message.delete()

    if not spam_allowed():
        return

    delaySpamEvent = Event()
    for i in range(0, count):
        if i != 0:
            delaySpamEvent.wait(delay)
        await client.send_message(message.chat.id, spam_message)
        limit = increment_spam_count()
        if not limit:
            break

    await client.send_message(
        BOTLOG_CHATID, "**#DELAYSPAM**\nDelaySpam was executed successfully"
    )


@Ubot(commands, cmds)
async def sspam(client: Client, message: Message):
    amount = int(message.command[1])
    text = " ".join(message.command[2:])

    cooldown = {"spam": 0.5, "statspam": 0.2, "slowspam": 0.8, "fspam": 0.1}

    await message.delete()

    for msg in range(amount):
        if message.reply_to_message:
            sent = await message.reply_to_message.reply(text)
        else:
            sent = await client.send_message(message.chat.id, text)

        if message.command[0] == "statspam":
            await asyncio.sleep(0.5)
            await sent.delete()

        await asyncio.sleep(cooldown[message.command[0]])


@Ubot(["dspam2"], cmds)
async def delayspammer(client, message):
    try:
        args = message.text.split(" ", 3)
        delay = float(args[1])
        count = int(args[2])
        msg = str(args[3])
    except BaseException:
        return await message.edit(f"**Penggunaan :** .dspam2 [delay] time] [count] [msg]")
    await message.delete()
    try:
        for i in range(count):
            await client.send_message(message.chat.id, msg)
            await asyncio.sleep(delay)
    except Exception as u:
        await client.send_message(message.chat.id, f"**Error :** `{u}`")
        
@Ubot(["spam2"], cmds)
async def spammer(client, message):
    text = message.text
    if message.reply_to_message:
        if not len(text.split()) >= 2:
            return await message.edit("`Gunakan dalam Format yang Tepat`")
        spam_message = message.reply_to_message
    else:
        if not len(text.split()) >= 3:
            return await message.edit("`Membalas Pesan atau Memberikan beberapa Teks ..`")
        spam_message = text.split(maxsplit=2)[2]
    counter = text.split()[1]
    try:
        counter = int(counter)
        if counter >= 100:
            return await message.edit("`Maksimal jumlah 100, Gunakan bspam untuk jumlah lebih dari 100`")
    except BaseException:
        return await message.edit("`Gunakan dalam Format yang Tepat`")
    await asyncio.wait([client.send_message(message.chat.id, spam_message) for i in range(counter)])
    await message.delete()


@Ubot(["bspam"], cmds)
async def bigspam(client, message):
    text = message.text
    if message.reply_to_message:
        if not len(text.split()) >= 2:
            return await message.edit("`Gunakan dalam Format yang Tepat` **Contoh** : bspam [jumlah] [kata]")
        spam_message = message.reply_to_message
    else:
        if not len(text.split()) >= 3:
            return await message.edit("`Membalas Pesan atau Memberikan beberapa Teks ..`")
        spam_message = text.split(maxsplit=2)[2]
    counter = text.split()[1]
    try:
        counter = int(counter)
    except BaseException:
        return await message.edit("`Gunakan dalam Format yang Tepat`")
    await asyncio.wait([client.send_message(message.chat.id, spam_message) for i in range(counter)])
    await message.delete()


@Ubot(["sspam"], cmds)
async def spam_stick(client: Client, message: Message):
    if not message.reply_to_message:
        await edit_or_reply(
            message, "**Reply to a sticker with amount you want to spam**"
        )
        return
    if not message.reply_to_message.sticker:
        await edit_or_reply(
            message, "**Reply to a sticker with amount you want to spam**"
        )
        return
    else:
        i = 0
        times = message.command[1]
        if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            for i in range(int(times)):
                sticker = message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id,
                    sticker,
                )
                await asyncio.sleep(0.10)

        if message.chat.type == enums.ChatType.PRIVATE:
            for i in range(int(times)):
                sticker = message.reply_to_message.sticker.file_id
                await client.send_sticker(message.chat.id, sticker)
                await asyncio.sleep(0.10)

add_command_help(
    "spam",
    [
        ["spam <jumlah spam> <text>", "Mengirim teks secara spam dalam obrolan!!"],
        ["spam2 <jumlah spam> <text>", "Mengirim teks secara spam dalam obrolan!!"],
        ["fspam <jumlah spam> <text>", "Mengirim spam secara cepat dalam obrolan!!"],
        [f"dspam [jumlah] [waktu delay] [kata kata]","Delay spam."],
        [f"sspam [balas ke stiker] [jumlah spam]","Spam stiker."],
        [f"dspam2","Khusus Anak RP. dspam2 <delay><jumlah><pesan>"],
        ["bspam <jumlah spam> <text>", "Mengirim teks secara spam dalam obrolan!!"],
    ],
)
