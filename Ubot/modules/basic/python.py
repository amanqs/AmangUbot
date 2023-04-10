# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

import asyncio
import pyromod
from io import BytesIO
import io
import os
import sys
import re
import traceback
import subprocess
from random import randint
from typing import Optional
from contextlib import suppress, redirect_stdout
from asyncio import sleep
from io import StringIO
from pyrogram.types import *
from pyrogram import *
from pyromod import *

from pyrogram import Client, filters
from pyrogram.types import Message


from . import *



# noinspection PyUnusedLocal
@Client.on_message(filters.command(["ex"], cmds) & filters.me)
async def user_exec(client: Client, message: Message):
    if message.from_user.id not in ADMINS:
        return await message.edit("**Lu bukan ADMINS**")
        
  
    if len(message.command) == 1:
        return await message.edit("<b>Code to execute isn't provided</b>")

    reply = message.reply_to_message

    code = message.text.split(maxsplit=1)[1]
    stdout = StringIO()

    await message.edit("<b>Executing...</b>")

    try:
        with redirect_stdout(stdout):
            exec(code)
        text = (
            "<b>Code:</b>\n"
            f"<pre language=python>{code}</pre>\n\n"
            "<b>Result</b>:\n"
            f"<code>{stdout.getvalue()}</code>"
        )
        if message.command[0] == "exnoedit":
            await message.reply(text)
        else:
            await message.edit(text)
    except Exception as e:
        await message.edit(format_exc(e, f"Code was <code>{code}</code>"))



@Client.on_message(filters.command(["ev"], cmds) & filters.me)
async def evaluation_cmd_t(client, message):
    if message.from_user.id not in ADMINS:
        return await message.edit("**Lu bukan ADMINS**")

    status_message = await message.edit("`Processing eval..`")
    try:
        cmd = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await status_message.edit("`Give commands !`")
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"

    final_output = f"""
**EVAL**:
```python
{cmd}
```

**OUTPUT**:
```python
{evaluation.strip()}
```
"""
    if len(final_output) > 4096:
        with open("eval.txt", "w+", encoding="utf8") as out_file:
            out_file.write(final_output)
        await status_message.reply_document(
            document="eval.txt",
            caption=cmd[: 4096 // 4 - 1],
            disable_notification=True,
        )
        os.remove("eval.txt")
        await status_message.delete()
    else:
        await status_message.edit(final_output, parse_mode=enums.ParseMode.MARKDOWN)
