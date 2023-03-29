

import os
import re
import sys
import asyncio
import traceback
import importlib
import subprocess
from io import BytesIO
from types import ModuleType
from typing import Dict

from PIL import Image
from pyrogram import Client, errors, types



META_COMMENTS = re.compile(r"^ *# *meta +(\S+) *: *(.*?)\s*$", re.MULTILINE)
interact_with_to_delete = []


def text(message: types.Message) -> str:
    """Find text in `types.Message` object"""
    return message.text if message.text else message.caption

async def aexec(code, c, m):
    exec(
        "async def __aexec(c, m): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](c, m)


async def shell_exec(code, treat=True):
    process = await asyncio.create_subprocess_shell(
        code, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT
    )

    stdout = (await process.communicate())[0]
    if treat:
        stdout = stdout.decode().strip()
    return stdout, process

def format_exc(e: Exception, suffix="") -> str:
    traceback.print_exc()
    if isinstance(e, errors.RPCError):
        return (
            f"<b>Telegram API error!</b>\n"
            f"<code>[{e.CODE} {e.ID or e.NAME}] — {e.MESSAGE.format(value=e.value)}</code>\n\n<b>{suffix}</b>"
        )
    return (
        f"<b>Error!</b>\n"
        f"<code>{e.__class__.__name__}: {e}</code>\n\n<b>{suffix}</b>"
    )


def with_reply(func):
    async def wrapped(client: Client, message: types.Message):
        if not message.reply_to_message:
            await message.edit("<b>Reply to message is required</b>")
        else:
            return await func(client, message)

    return wrapped


async def interact_with(message: types.Message) -> types.Message:
    """
    Check history with bot and return bot's response

    Example:
    .. code-block:: python
        bot_msg = await interact_with(await bot.send_message("@BotFather", "/start"))
    :param message: already sent message to bot
    :return: bot's response
    """

    await asyncio.sleep(1)
    # noinspection PyProtectedMember
    response = [
        msg
        async for msg in message._client.get_chat_history(
            message.chat.id, limit=1
        )
    ]
    seconds_waiting = 0

    while response[0].from_user.is_self:
        seconds_waiting += 1
        if seconds_waiting >= 5:
            raise RuntimeError("bot didn't answer in 5 seconds")

        await asyncio.sleep(1)
        # noinspection PyProtectedMember
        response = [
            msg
            async for msg in message._client.get_chat_history(
                message.chat.id, limit=1
            )
        ]

    interact_with_to_delete.append(message.id)
    interact_with_to_delete.append(response[0].id)

    return response[0]




def resize_image(
    input_img, output=None, img_type="PNG", size: int = 512, size2: int = None
):
    if output is None:
        output = BytesIO()
        output.name = f"sticker.{img_type.lower()}"

    with Image.open(input_img) as img:
        # We used to use thumbnail(size) here, but it returns with a *max* dimension of 512,512
        # rather than making one side exactly 512, so we have to calculate dimensions manually :(
        if size2 is not None:
            size = (size, size2)
        elif img.width == img.height:
            size = (size, size)
        elif img.width < img.height:
            size = (max(size * img.width // img.height, 1), size)
        else:
            size = (size, max(size * img.height // img.width, 1))

        img.resize(size).save(output, img_type)

    return output


def parse_meta_comments(code: str) -> Dict[str, str]:
    try:
        groups = META_COMMENTS.search(code).groups()
    except AttributeError:
        return {}

    return {groups[i]: groups[i + 1] for i in range(0, len(groups), 2)}
