from pyrogram.types import InlineKeyboardButton
from config import *

def song_markup(_, vidid):
    buttons = [
        [
            
            InlineKeyboardButton(
                 "ᴠᴇʀᴏɴ", url=SUPPORT_CHANNEL
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["SG_B_2"],
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["SG_B_3"],
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons
