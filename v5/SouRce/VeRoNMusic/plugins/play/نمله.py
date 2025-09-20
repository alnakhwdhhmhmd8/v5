from pyrogram import enums, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from VeRoNMusic import app

# دالة لاختبار قفل الألعاب
def lock_games_test(message):
    return False  # قم بتعديلها حسب نظامك

@app.on_message(filters.text & filters.private)
async def handle_games(client, message):
    text = message.text

    if text in ["نمله", "النمله"]:
        if not lock_games_test(message):
            keyboard = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🐜", callback_data="antgame")]]
            )
            await message.reply_photo("https://t.me/UUSDI55/41", reply_markup=keyboard)
        else:
            await message.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√")

    elif text in ["صرصار", "صرصور", "الصرصار"]:
        if not lock_games_test(message):
            keyboard = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🦗", callback_data="cockroachgame")]]
            )
            await message.reply_photo("https://t.me/UUSDI55/42", reply_markup=keyboard)
        else:
            await message.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√")

    elif text in ["خنزير", "خنزيره", "الخنزير"]:
        if not lock_games_test(message):
            keyboard = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🐷", callback_data="piggame")]]
            )
            await message.reply_photo("https://t.me/UUSDI55/43", reply_markup=keyboard)
        else:
            await message.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√")

@app.on_callback_query(filters.regex("^antgame$"))
async def antgame_callback(client, callback_query):
    await callback_query.answer("ياكلب ياللي معندكش رحمه بتموتها لي..😒😢", show_alert=True)
    await callback_query.message.delete()
    await callback_query.message.reply_photo(
        "https://t.me/UUSDI55/44",
        caption=f"هو الكلب ده اللي موتها يجماعه😂👇\n[{callback_query.from_user.first_name}](tg://user?id={callback_query.from_user.id})",
        parse_mode=enums.ParseMode.MARKDOWN
    )

@app.on_callback_query(filters.regex("^cockroachgame$"))
async def cockroachgame_callback(client, callback_query):
    await callback_query.answer("يخربييت ام دى عفانه..😒😢", show_alert=True)
    await callback_query.message.delete()
    await callback_query.message.reply_animation(
        "https://t.me/UUSDI55/45",
        caption=f"هو المعفن اللى صحي الصرصار يجماعه😂👇\n[{callback_query.from_user.first_name}](tg://user?id={callback_query.from_user.id})",
        parse_mode=enums.ParseMode.MARKDOWN
    )

@app.on_callback_query(filters.regex("^piggame$"))
async def piggame_callback(client, callback_query):
    await callback_query.answer("قتلت اخوك ياخنزير..😒😢", show_alert=True)
    await callback_query.message.delete()
    await callback_query.message.reply_photo(
        "https://t.me/UUSDI55/46",
        caption=f"هو الخنزير اللى قتل اخوه يجماعه😂👇\n[{callback_query.from_user.first_name}](tg://user?id={callback_query.from_user.id})",
        parse_mode=enums.ParseMode.MARKDOWN
    )