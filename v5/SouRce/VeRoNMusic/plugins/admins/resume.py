from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from VeRoNMusic import app
from VeRoNMusic.core.call import KIM
from strings import get_string
from VeRoNMusic.utils.database.memorydatabase import is_music_playing, music_on
from VeRoNMusic.utils.decorators import AdminRightsCheck

# Commands
RESUME_COMMAND = get_command("RESUME_COMMAND")





@app.on_message(filters.command(["resume", "cresume"]) & filters.channel)
@app.on_message(filters.command(["كمل"],"") & filters.channel)
async def resume_comcc(cli, message):
    _ = get_string("en")
    chat_id = message.chat.id
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    await KIM.resume_stream(chat_id)
    await message.reply_text(_["admin_4"].format(message.chat.title))
    
    
    
    
@app.on_message(filters.command(["كمل"],"") & filters.group & ~BANNED_USERS, group=544)
@app.on_message(filters.command(RESUME_COMMAND) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    await KIM.resume_stream(chat_id)
    await message.reply_text(_["admin_4"].format(message.from_user.mention))
