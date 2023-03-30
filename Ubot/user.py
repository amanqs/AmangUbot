
from ast import parse
from pyrogram import (
    Client,
    __version__,
    enums
)
from Ubot.logging import LOGGER
from config import *


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
        self.LOGGER = LOGGER
        

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
        self.LOGGER = LOGGER
        

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
        self.LOGGER = LOGGER
        

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
        self.LOGGER = LOGGER
        

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
        self.LOGGER = LOGGER
        

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
        self.LOGGER = LOGGER
        

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
        self.LOGGER = LOGGER
        

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
        self.LOGGER = LOGGER
        

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
        self.LOGGER = LOGGER
        

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
        self.LOGGER = LOGGER
        

class User11(Client):
    def __init__(self):
        super().__init__(
            name="bot11",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION11,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        self.LOGGER = LOGGER
        

class User12(Client):
    def __init__(self):
        super().__init__(
            name="bot12",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION12,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        self.LOGGER = LOGGER
        

class User13(Client):
    def __init__(self):
        super().__init__(
            name="bot13",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION13,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        self.LOGGER = LOGGER
        

class User14(Client):
    def __init__(self):
        super().__init__(
            name="bot14",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION14,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        self.LOGGER = LOGGER
        

class User15(Client):
    def __init__(self):
        super().__init__(
            name="bot15",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION15,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        self.LOGGER = LOGGER
        

class User16(Client):
    def __init__(self):
        super().__init__(
            name="bot16",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION16,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        self.LOGGER = LOGGER
        

class User17(Client):
    def __init__(self):
        super().__init__(
            name="bot17",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION17,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        self.LOGGER = LOGGER
        

class User18(Client):
    def __init__(self):
        super().__init__(
            name="bot18",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION18,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        self.LOGGER = LOGGER
        

class User19(Client):
    def __init__(self):
        super().__init__(
            name="bot19",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION19,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        self.LOGGER = LOGGER
        

class User20(Client):
    def __init__(self):
        super().__init__(
            name="bot20",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION20,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        self.LOGGER = LOGGER
        

class User21(Client):
    def __init__(self):
        super().__init__(
            name="bot21",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION21,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
            no_updates=True,
        )
        

class User22(Client):
    def __init__(self):
        super().__init__(
            name="bot22",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION22,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
            no_updates=True,
        )
        

class User23(Client):
    def __init__(self):
        super().__init__(
            name="bot23",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION23,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
            no_updates=True,
        )
        

class User24(Client):
    def __init__(self):
        super().__init__(
            name="bot24",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION24,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
            no_updates=True,
        )
        

class User25(Client):
    def __init__(self):
        super().__init__(
            name="bot25",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION25,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
            no_updates=True,
        )
        

class User26(Client):
    def __init__(self):
        super().__init__(
            name="bot26",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION26,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
            no_updates=True,
        )
        

class User27(Client):
    def __init__(self):
        super().__init__(
            name="bot27",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION27,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
            no_updates=True,
        )
        

class User28(Client):
    def __init__(self):
        super().__init__(
            name="bot28",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION28,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
            no_updates=True,
        )
        

class User29(Client):
    def __init__(self):
        super().__init__(
            name="bot29",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION29,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
            no_updates=True,
        )
        

class User30(Client):
    def __init__(self):
        super().__init__(
            name="bot30",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION30,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        self.LOGGER = LOGGER
        
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