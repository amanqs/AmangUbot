
import traceback
import re
from pyrogram import Client, filters
from pyrogram.errors import MessageDeleteForbidden
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from Ubot import CMD_HELP, app
from Ubot.core import *
from Ubot import ids as users
from config import SUPPORT, CHANNEL


@Client.on_callback_query()
async def _callbacks(_, callback_query: CallbackQuery):
    query = callback_query.data.lower()
    bot_me = await app.get_me()
    if query == "helper":
        buttons = paginate_help(0, CMD_HELP, "helpme")
        await app.edit_inline_text(
            callback_query.inline_message_id,
            Data.text_help_menu,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif query == "close":
        await app.edit_inline_text(callback_query.inline_message_id, "**ᴄʟᴏsᴇ**")
        return
    elif query == "close_help":
        await app.edit_inline_text(
            callback_query.inline_message_id,
            "**ᴄʟᴏsᴇ**",
            reply_markup=InlineKeyboardMarkup(Data.reopen),
        )
        return
    elif query == "closed":
        try:
            await callback_query.message.delete()
        except BaseException:
            pass
        try:
            await callback_query.message.reply_to_message.delete()
        except BaseException:
            pass
    elif query == "make_basic_button":
        try:
            bttn = paginate_help(0, CMD_HELP, "helpme")
            await app.edit_inline_text(
                callback_query.inline_message_id,
                Data.text_help_menu,
                reply_markup=InlineKeyboardMarkup(bttn),
            )
        except Exception as e:
            e = traceback.format_exc()
            print(e, "Callbacks")
    elif query.startswith("helpme_prev"):
        current_page_number = int(re.findall(r'\((.*?)\)', query)[0])
        buttons = paginate_help(current_page_number - 1, CMD_HELP, "helpme")
        await app.edit_inline_text(
            callback_query.inline_message_id,
            Data.text_help_menu,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif query.startswith("helpme_next"):
        current_page_number = int(re.findall(r'\((.*?)\)', query)[0])
        buttons = paginate_help(current_page_number + 1, CMD_HELP, "helpme")
        await app.edit_inline_text(
            callback_query.inline_message_id,
            Data.text_help_menu,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif query.startswith("reopen"):
        buttons = paginate_help(0, CMD_HELP, "helpme")
        await app.edit_inline_text(
            callback_query.inline_message_id,
            Data.text_help_menu,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif query.startswith("ub_modul_"):
        modul_name = query.replace("ub_modul_", "")
        commands: dict = CMD_HELP[modul_name]
        this_command = f"**Bantuan Untuk {str(modul_name).upper()}**\n\n"
        for x in commands:
            this_command += f"๏ **Perintah:** `{str(x)}`\n◉ **Keterangan:** `{str(commands[x])}`\n\n"
        this_command += ""
        bttn = [
            [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="reopen")],
        ]
        reply_pop_up_alert = (
            this_command
            if this_command is not None
            else f"{modul_name} Belum ada penjelasannya ."
        )
        await app.edit_inline_text(
            callback_query.inline_message_id,
            reply_pop_up_alert,
            reply_markup=InlineKeyboardMarkup(bttn),
        )
