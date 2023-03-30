import sys
from ast import parse
from pyrogram import (
    Client,
    __version__,
    enums
)
from .logging import LOGGER
from config import API_ID, API_HASH, BOT_TOKEN, BOT_WORKERS
from config import SESSION1, SESSION2, SESSION3, SESSION4, SESSION5, SESSION6, SESSION7, SESSION8, SESSION9, SESSION10


class User1(Client):
    def __init__(self):
        super().__init__(
            name="bot1",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION1,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION1:
            self.LOGGER = LOGGER
        else:
            LOGGER(__name__).warning("STRING SESSION TIDAK DITEMUKAN, SHUTDOWN BOT!")
            sys.exit()

class User2(Client):
    def __init__(self):
        super().__init__(
            name="bot2",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION2,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION2:
            self.LOGGER = LOGGER
        else:
            LOGGER(__name__).warning("STRING SESSION TIDAK DITEMUKAN, SHUTDOWN BOT!")
            sys.exit()

class User3(Client):
    def __init__(self):
        super().__init__(
            name="bot3",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION3,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION3:
            self.LOGGER = LOGGER
        else:
            LOGGER(__name__).warning("STRING SESSION TIDAK DITEMUKAN, SHUTDOWN BOT!")
            sys.exit()

class User4(Client):
    def __init__(self):
        super().__init__(
            name="bot4",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION4,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION4:
            self.LOGGER = LOGGER
        else:
            None

class User5(Client):
    def __init__(self):
        super().__init__(
            name="bot5",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION5,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION5:
            self.LOGGER = LOGGER
        else:
            None

class User6(Client):
    def __init__(self):
        super().__init__(
            name="bot6",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION6,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION6:
            self.LOGGER = LOGGER
        else:
            None

class User7(Client):
    def __init__(self):
        super().__init__(
            name="bot7",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION7,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION7:
            self.LOGGER = LOGGER
        else:
            None

class User8(Client):
    def __init__(self):
        super().__init__(
            name="bot8",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION8,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION8:
            self.LOGGER = LOGGER
        else:
            None

class User9(Client):
    def __init__(self):
        super().__init__(
            name="bot9",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION9,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION9:
            self.LOGGER = LOGGER
        else:
            None

class User10(Client):
    def __init__(self):
        super().__init__(
            name="bot10",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION10,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION10:
            self.LOGGER = LOGGER
        else:
            None

    async def start(self):
        await super().start()
        usr_bot_me = self.me
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} based on Pyrogram v{__version__} "
        )
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
