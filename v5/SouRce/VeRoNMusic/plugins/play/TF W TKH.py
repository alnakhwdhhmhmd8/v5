from pyrogram import Client, filters
from random import choice, randint
from VeRoNMusic import app
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)

@app.on_message(filters.command("تخ", [".", ""]) & filters.group & filters.reply, group=75365)
async def kill_animation(client, message):
    if not message.reply_to_message or not message.reply_to_message.from_user:
        await message.reply("يرجى الرد على رسالة المستخدم لتنفيذ الأمر.")
        return

    await message.reply_animation(
        animation="https://telegra.ph/file/b90d4b29a715fb542544a.mp4",
        caption=f"""≭︰قتل ↫ ⦗ {message.from_user.mention} ⦘\n≭︰الضحيه دا 😢 ↫ ⦗ {message.reply_to_message.from_user.mention} ⦘\nانا لله وانـا اليـه راجعـون 😢😢""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المقتول 🔪", url=f"https://t.me/{message.reply_to_message.from_user.username}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "‹ 𝖲𝗈𝖴𝗋𝖼𝖾 VeRoN ›", url="https://t.me/Source_Veron"
                    )
                ],
            ]
        )
    )

@app.on_message(filters.command("تف", [".", ""]) & filters.group & filters.reply, group=7865)
async def spit_animation(client, message):
    if not message.reply_to_message or not message.reply_to_message.from_user:
        await message.reply("يرجى الرد على رسالة المستخدم لتنفيذ الأمر.")
        return

    await message.reply_animation(
        animation="https://telegra.ph/file/4a1f6a9bacb1a863f03f1.mp4",
        caption=f"""≭︰تف ↫ ⦗ {message.from_user.mention} ⦘\n≭︰علي الضحيه دا 😢 ↫ ⦗ {message.reply_to_message.from_user.mention} ⦘\nاععع اي القرف دا""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المجني عليه 😢", url=f"https://t.me/{message.reply_to_message.from_user.username}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "‹ 𝖲𝗈𝖴𝗋𝖼𝖾 VeRoN ›", url="https://t.me/Source_Veron"
                    )
                ],
            ]
        )
    )

@app.on_message(filters.command("مح", [".", ""]) & filters.group & filters.reply, group=7565)
async def kiss_animation(client, message):
    if not message.reply_to_message or not message.reply_to_message.from_user:
        await message.reply("يرجى الرد على رسالة المستخدم لتنفيذ الأمر.")
        return

    await message.reply_animation(
        animation="https://telegra.ph/file/3dd136786231ab017bd53.mp4",
        caption=f"""الجميل هذا ✨♥↫ ⦗ {message.from_user.mention} ⦘\nبعتلك بوسه يا 😘♥ ↫ ⦗ {message.reply_to_message.from_user.mention} ⦘\n عيب كده اي المحن ده 😹""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المتباس 💋", url=f"https://t.me/{message.reply_to_message.from_user.username}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "‹ 𝖲𝗈𝖴𝗋𝖼𝖾 VeRoN ›", url="https://t.me/Source_Veron"
                    )
                ],
            ]
        )
    )