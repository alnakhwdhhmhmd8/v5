from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from VeRoNMusic import app
import config
from pyrogram.errors import FloodWait




@app.on_message(filters.command(["عاوز انصب","عاوزه انصب","تنصيب","التنصيب","ميوزك","الميوزك"], ""), group=6535585)
async def maker(client: Client, message: Message):
     await message.reply_video(
        video="https://h.uguu.se/NuRwKkaV.mp4",
        caption="⌯ للتنصيب تواصـل مع فيࢪون ❲ [اضغط هنا](https://t.me/ToxVe) ❳ \n\n√",
            reply_markup=InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
