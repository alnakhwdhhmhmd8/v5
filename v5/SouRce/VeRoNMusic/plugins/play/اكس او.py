from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import random
from VeRoNMusic import app 


games = {}

def start_board():
    return [' ' for _ in range(9)]

def draw_board(board):
    return f"""
{board[0]} | {board[1]} | {board[2]}
---------
{board[3]} | {board[4]} | {board[5]}
---------
{board[6]} | {board[7]} | {board[8]}
"""

def check_winner(board, player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for line in wins:
        if all(board[i] == player for i in line):
            return True
    return False

def create_buttons(board, restart=False):
    buttons = []
    if restart:
        buttons.append([InlineKeyboardButton("🔄 إعادة", callback_data="restart")])
        return InlineKeyboardMarkup(buttons)
    for i in range(0, 9, 3):
        row = []
        for j in range(3):
            idx = i + j
            text = board[idx] if board[idx] != ' ' else str(idx+1)
            row.append(InlineKeyboardButton(text=text, callback_data=f"move_{idx}"))
        buttons.append(row)
    return InlineKeyboardMarkup(buttons)

@app.on_message(filters.text & filters.regex(r"^(xo|اكس او)$"))
async def start_pvp_game(client, message: Message):
    chat_id = message.chat.id
    games[chat_id] = {
        "board": start_board(),
        "turn": "X",
        "players": [message.from_user.id],
        "vs_bot": False,
        "difficulty": None
    }
    await message.reply(
        f"🎮 لعبة XO جديدة بين لاعبين!\n\n{draw_board(games[chat_id]['board'])}\nالدور: X\nأول من يلعب سيكون X، والثاني سيكون O.",
        reply_markup=create_buttons(games[chat_id]["board"])
    )

@app.on_message(filters.text & filters.regex(r"^(xob|اكس او بوت)$"))
async def start_pvb_game(client, message: Message):
    chat_id = message.chat.id
    games[chat_id] = {
        "board": start_board(),
        "turn": "X",
        "players": [message.from_user.id],
        "vs_bot": True,
        "difficulty": None
    }
    await message.reply(
        "🎮 اختر مستوى الصعوبة:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🟢 سهل", callback_data="difficulty_easy")],
            [InlineKeyboardButton("🟠 متوسط", callback_data="difficulty_medium")],
            [InlineKeyboardButton("🔴 صعب", callback_data="difficulty_hard")]
        ])
    )

@app.on_callback_query(filters.regex(r"difficulty_(easy|medium|hard)"))
async def set_difficulty(client, callback_query):
    chat_id = callback_query.message.chat.id
    difficulty = callback_query.data.split("_")[1]
    if chat_id in games:
        games[chat_id]["difficulty"] = difficulty
        await callback_query.edit_message_text(
            f"🎮 لعبة XO ضد البوت - مستوى {difficulty}!\n\n{draw_board(games[chat_id]['board'])}\nالدور: X",
            reply_markup=create_buttons(games[chat_id]["board"])
        )
    await callback_query.answer()

@app.on_callback_query(filters.regex(r"move_(\d)"))
async def handle_move(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    if chat_id not in games:
        await callback_query.answer("❌ لا توجد لعبة جارية.", show_alert=True)
        return

    game = games[chat_id]
    idx = int(callback_query.data.split("_")[1])

    if game["board"][idx] != ' ':
        await callback_query.answer("❌ هذه الخانة مشغولة.", show_alert=True)
        return

    # لاعب ضد لاعب
    if not game["vs_bot"]:
        if len(game["players"]) == 1 and user_id != game["players"][0]:
            game["players"].append(user_id)
            await callback_query.answer(f"✅ أنت الآن لاعب O", show_alert=False)
        if user_id != game["players"][0] and (len(game["players"]) < 2 or user_id != game["players"][1]):
            await callback_query.answer("❌ هذه ليست لعبتك!", show_alert=True)
            return
        expected_turn = game["players"][0] if game["turn"] == "X" else game["players"][1]
        if user_id != expected_turn:
            await callback_query.answer("❌ ليس دورك!", show_alert=True)
            return
        game["board"][idx] = game["turn"]
        board_text = draw_board(game["board"])
        if check_winner(game["board"], game["turn"]):
            await callback_query.edit_message_text(f"🎉 الفائز: {game['turn']}!\n\n{board_text}", reply_markup=create_buttons(game["board"], restart=True))
            games.pop(chat_id)
            return
        if all(cell != ' ' for cell in game["board"]):
            await callback_query.edit_message_text(f"🤝 تعادل!\n\n{board_text}", reply_markup=create_buttons(game["board"], restart=True))
            games.pop(chat_id)
            return
        game["turn"] = "O" if game["turn"] == "X" else "X"
        await callback_query.edit_message_text(f"{board_text}\nالدور: {game['turn']}", reply_markup=create_buttons(game["board"]))
        await callback_query.answer()
        return

    # لاعب ضد البوت
    if game["difficulty"] is None:
        await callback_query.answer("❌ اختر مستوى الصعوبة أولاً.", show_alert=True)
        return
    if user_id != game["players"][0]:
        await callback_query.answer("❌ هذه ليست لعبتك!", show_alert=True)
        return

    game["board"][idx] = "X"
    board_text = draw_board(game["board"])
    if check_winner(game["board"], "X"):
        await callback_query.edit_message_text(f"🎉 الفائز: X!\n\n{board_text}", reply_markup=create_buttons(game["board"], restart=True))
        games.pop(chat_id)
        return
    if all(cell != ' ' for cell in game["board"]):
        await callback_query.edit_message_text(f"🤝 تعادل!\n\n{board_text}", reply_markup=create_buttons(game["board"], restart=True))
        games.pop(chat_id)
        return
    game["turn"] = "O"
    await callback_query.edit_message_text(f"{board_text}\nالدور: O (بوت)", reply_markup=create_buttons(game["board"]))
    await bot_move(client, callback_query.message, game)
    await callback_query.answer()

async def bot_move(client, message, game):
    difficulty = game["difficulty"]
    if difficulty == "easy":
        idx = random.choice([i for i, cell in enumerate(game["board"]) if cell == ' '])
    elif difficulty == "medium":
        idx = bot_smart_move(game["board"])
    else:
        idx = bot_hard_move(game["board"])
    game["board"][idx] = "O"
    board_text = draw_board(game["board"])
    if check_winner(game["board"], "O"):
        await message.edit_text(f"🎉 الفائز: O (بوت)!\n\n{board_text}", reply_markup=create_buttons(game["board"], restart=True))
        games.pop(message.chat.id)
        return
    if all(cell != ' ' for cell in game["board"]):
        await message.edit_text(f"🤝 تعادل!\n\n{board_text}", reply_markup=create_buttons(game["board"], restart=True))
        games.pop(message.chat.id)
        return
    game["turn"] = "X"
    await message.edit_text(f"{board_text}\nالدور: X", reply_markup=create_buttons(game["board"]))

def bot_smart_move(board):
    empty = [i for i, cell in enumerate(board) if cell == ' ']
    for idx in empty:
        board_copy = board.copy()
        board_copy[idx] = 'O'
        if check_winner(board_copy, 'O'):
            return idx
    for idx in empty:
        board_copy = board.copy()
        board_copy[idx] = 'X'
        if check_winner(board_copy, 'X'):
            return idx
    if 4 in empty:
        return 4
    for idx in [0, 2, 6, 8]:
        if idx in empty:
            return idx
    return random.choice(empty)

def bot_hard_move(board):
    def minimax(board, depth, is_maximizing):
        if check_winner(board, 'O'):
            return 10 - depth
        if check_winner(board, 'X'):
            return depth - 10
        if all(cell != ' ' for cell in board):
            return 0
        scores = []
        for idx, cell in enumerate(board):
            if cell == ' ':
                board[idx] = 'O' if is_maximizing else 'X'
                score = minimax(board, depth+1, not is_maximizing)
                board[idx] = ' '
                scores.append(score)
        return max(scores) if is_maximizing else min(scores)
    best_score = -float('inf')
    best_move = None
    for idx, cell in enumerate(board):
        if cell == ' ':
            board[idx] = 'O'
            score = minimax(board, 0, False)
            board[idx] = ' '
            if score > best_score:
                best_score = score
                best_move = idx
    return best_move

@app.on_callback_query(filters.regex(r"restart"))
async def restart_game(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    games[chat_id] = {
        "board": start_board(),
        "turn": "X",
        "players": [user_id],
        "vs_bot": False,
        "difficulty": None
    }
    await callback_query.edit_message_text(f"🎮 لعبة XO جديدة بين لاعبين!\n\n{draw_board(games[chat_id]['board'])}\nالدور: X\nأول من يلعب سيكون X، والثاني سيكون O.",
                                           reply_markup=create_buttons(games[chat_id]["board"]))
    await callback_query.answer("🔄 تم إعادة اللعبة!")
