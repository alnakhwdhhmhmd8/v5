import random

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from strings import get_string
from VeRoNMusic import app
from VeRoNMusic.misc import db
from VeRoNMusic.utils.decorators import AdminRightsCheck

# Commands
SHUFFLE_COMMAND = get_command("SHUFFLE_COMMAND")

@app.on_message(filters.command(["shuffle", "cshuffle"]) & filters.channel)
@app.on_message(filters.command(["خلط","دمج"],"") & filters.channel)
async def admins_comcc(cli, message):
    _ = get_string("en")
    chat_id = message.chat.id
    check = db.get(chat_id)
    if not check:
        return await message.reply_text(_["admin_21"])
    try:
        popped = check.pop(0)
    except:
        return await message.reply_text(_["admin_22"])
    check = db.get(chat_id)
    if not check:
        check.insert(0, popped)
        return await message.reply_text(_["admin_22"])
    random.shuffle(check)
    check.insert(0, popped)
    await message.reply_text(_["admin_23"].format(message.chat.title))
    
    
    
    
    
@app.on_message(filters.command(SHUFFLE_COMMAND) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
@app.on_message(filters.command(["خلط","دمج"],"") & filters.group, group=6566)
async def admins(Client, message: Message, _, chat_id):
    check = db.get(chat_id)
    if not check:
        return await message.reply_text(_["admin_21"])
    try:
        popped = check.pop(0)
    except:
        return await message.reply_text(_["admin_22"])
    check = db.get(chat_id)
    if not check:
        check.insert(0, popped)
        return await message.reply_text(_["admin_22"])
    random.shuffle(check)
    check.insert(0, popped)
    await message.reply_text(_["admin_23"].format(message.from_user.first_name))
