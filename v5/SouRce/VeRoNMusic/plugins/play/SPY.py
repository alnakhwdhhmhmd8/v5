from VeRoNMusic import app
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

game_started = False
game_players = []
spy = None
game_starter = None
category_word = None
locations = ["مصر", "السعودية", "الولايات المتحدة", "فرنسا", "اليابان"]
foods = ["بيتزا", "سوشي", "برجر", "باستا", "سلطة"]
drinks_and_fruits = ["قهوة", "شاي", "عصير", "صودا", "ماء", "تفاحة", "موز", "برتقالة", "عنب", "فراولة"]

@app.on_message(filters.regex("^جاسوس$") & filters.group, group=86734)
async def spy_command(client, message):
    global game_started, game_players
    if not game_started:
        if message.from_user.id not in game_players:
            game_players.append(message.from_user.id)
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("الانضمام للعبة", callback_data="join"),
                InlineKeyboardButton("بدء اللعبة", callback_data="start_game")
            ]
        ])
        await message.reply(f"تم انضمام {len(game_players)} إلى اللعبة. اضغط ابدأ عند اكتمال اللاعبين.", reply_markup=keyboard)
    else:
        await message.reply("اللعبة قيد التشغيل بالفعل. يرجى الانتظار للدور القادم.")

@app.on_callback_query(filters.regex("^join$"), group=765801)
async def join_game(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id in game_players:
        await callback_query.answer("أنت مشترك بالفعل في اللعبة.")
    else:
        game_players.append(user_id)
        await callback_query.answer("لقد انضممت للعبة.")
        await callback_query.message.edit_text(
            f"تم انضمام {len(game_players)} إلى اللعبة. اضغط ابدأ عند اكتمال اللاعبين.",
            reply_markup=callback_query.message.reply_markup
        )

@app.on_callback_query(filters.regex("^start_game$"), group=765800)
async def start_game(client, callback_query):
    global game_started, game_players, spy, game_starter
    if not game_started:
        if len(game_players) < 3:
            await callback_query.answer("يجب أن يكون هناك 3 أشخاص على الأقل لبدء اللعبة.")
            return
        game_started = True
        spy = random.choice(game_players)
        game_starter = callback_query.from_user.id
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("الأماكن", callback_data="places")],
            [InlineKeyboardButton("الأطعمة", callback_data="foods")],
            [InlineKeyboardButton("المشروبات والفواكه", callback_data="drinks_and_fruits")]
        ])
        message_text = f"تم انضمام {len(game_players)} للعبة. اضغط على الخيار المناسب."
        for player in game_players:
            if player == spy:
                await client.send_message(player, "أنت الجاسوس!")
            else:
                await client.send_message(player, message_text, reply_markup=keyboard)
        await callback_query.message.edit_text("تم بدء اللعبة. اختر فئة الكلمة من الأماكن، الأطعمة، أو المشروبات والفواكه.", reply_markup=None)
    else:
        await callback_query.answer("اللعبة قيد التشغيل بالفعل. يرجى الانتظار للدور القادم.")

@app.on_callback_query(filters.regex("^(places|foods|drinks_and_fruits)$"), group=765799)
async def choose_category(client, callback_query):
    global category_word
    category_word = callback_query.data
    if category_word == "places":
        word = random.choice(locations)
    elif category_word == "foods":
        word = random.choice(foods)
    elif category_word == "drinks_and_fruits":
        word = random.choice(drinks_and_fruits)
    else:
        await callback_query.answer("فئة غير معروفة.")
        return

    message_text = f"الكلمة هي: {word}"
    for player in game_players:
        if player == spy:
            await client.send_message(player, "أنت الجاسوس!")
        else:
            await client.send_message(player, message_text)
    await callback_query.answer("تم اختيار الكلمة وإرسالها لجميع المشتركين.")

@app.on_callback_query(filters.regex("^vote_for_spy$"), group=765797)
async def vote_for_spy(client, callback_query):
    buttons = []
    for user_id in game_players:
        user = await client.get_users(user_id)
        buttons.append([InlineKeyboardButton(user.first_name, callback_data=f"vote_{user_id}")])
    keyboard = InlineKeyboardMarkup(buttons)
    await callback_query.message.edit_text("التصويت: من هو الجاسوس؟", reply_markup=keyboard)

@app.on_callback_query(filters.regex("^vote_"), group=765798)
async def handle_vote(client, callback_query):
    voted_user_id = int(callback_query.data.split("_")[1])
    if voted_user_id == spy:
        spy_user = await client.get_users(spy)
        await callback_query.answer(f"تم التصويت بنجاح. الجاسوس هو: {spy_user.first_name}")
    else:
        await callback_query.answer("غلط يا فنان راحت عليك!")

if __name__ == "__main__":
    app.run()