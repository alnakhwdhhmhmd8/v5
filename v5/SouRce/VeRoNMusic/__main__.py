
import asyncio
import importlib

from pyrogram import idle

import config
from config import BANNED_USERS
from VeRoNMusic import HELPABLE, LOGGER, app, userbot
from VeRoNMusic.core.call import KIM
from VeRoNMusic.plugins import ALL_MODULES
from VeRoNMusic.utils.database import get_banned_users, get_gbanned


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("VeRoNMusic").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        # return
    if not config.SPOTIFY_CLIENT_ID and not config.SPOTIFY_CLIENT_SECRET:
        LOGGER("VeRoNMusic").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        imported_module = importlib.import_module(all_module)

        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELPABLE[imported_module.__MODULE__.lower()] = imported_module
    LOGGER("VeRoNMusic.plugins").info("Successfully Imported All Modules ")
    await userbot.start()
    await KIM.start()
    await KIM.decorators()
    LOGGER("VeRoNMusic").info("\x53\x6f\x75\x72\x63\x65\x20\x63\x6f\x64\x65\x20\x77\x61\x73\x20\x64\x65\x76\x65\x6c\x6f\x70\x65\x64\x20\x62\x79\x3a\x20\x40\x54\x6f\x70\x56\x65\x47\x61")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop_policy().get_event_loop().run_until_complete(init())
    LOGGER("VeRoNMusic").info("Stopping VeRoNMusic! GoodBye")
print("""

  ██╗       ██╗  ███████╗ ██████╗      ██████╗          ███╗       ██╗
  ██║       ██║  ██╔════╝ ██╔══██╗   ██╔═══██╗    ████╗     ██║
  ██║       ██║  █████╗       ██████╔╝   ██║        ██║    ██╔██╗   ██║
  ╚██╗ ██╔╝  ██╔══╝        ██╔══██╗  ██║        ██║    ██║╚██╗ ██║
    ╚████╔╝    ███████╗   ██║     ██║ ╚██████╔╝    ██║    ╚████║
       ╚═══╝       ╚══════╝   ╚═╝     ╚═╝    ╚═════╝      ╚═╝       ╚═══╝

  """)