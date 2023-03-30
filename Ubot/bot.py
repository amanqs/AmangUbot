
from pyrogram import (
    Client,
    __version__,
    enums
)
from .logging import LOGGER
import sys
from config import API_ID, API_HASH, BOT_TOKEN, BOT_WORKERS


class Bot(Client):
    """ modded client for SessionMakerBot """

    def __init__(self):
        super().__init__(
            name="ubot",
            api_hash=API_HASH,
            api_id=API_ID,
            bot_token=BOT_TOKEN,
            plugins={
                "root": "Ubot/modules/bot"
            },
            workers=BOT_WORKERS,
        )
#        if not BOT_TOKEN:
        self.LOGGER = LOGGER
#        else:
 #           LOGGER(__name__).error("WARNING: BOT TOKEN TIDAK DITEMUKAN, SHUTDOWN BOT")
  #          sys.exit()

    async def start(self):
        await super().start()
        usr_bot_me = self.me
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} based on Pyrogram v{__version__} "
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("SessionMakerBot stopped. Bye.")
