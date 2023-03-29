from pyrogram.types import InlineKeyboardButton, WebAppInfo
from Ubot import CMD_HNDLR as cmds
class Data:

    text_help_menu = (
        f"**Help Menu**\n** • Prefixes** : `None`"
    )
    reopen = [[InlineKeyboardButton("Open", callback_data="reopen")]]
