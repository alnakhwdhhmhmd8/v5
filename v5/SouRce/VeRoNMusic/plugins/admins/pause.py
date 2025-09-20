from pyrogram import filters
from pyrogram.types import Message
from strings import get_string
from config import BANNED_USERS
from strings import get_command
from VeRoNMusic import app
from VeRoNMusic.core.call import KIM
from VeRoNMusic.utils.database import is_music_playing, music_off
from VeRoNMusic.utils.decorators import AdminRightsCheck

# Commands
PAUSE_COMMAND = get_command("PAUSE_COMMAND")


    
@app.on_message(filters.command(["وقف","اسكت"],"") & filters.group & ~BANNED_USERS, group=6655098)
@app.on_message(filters.command(PAUSE_COMMAND) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await KIM.pause_stream(chat_id)
    await message.reply_text(_["admin_2"].format(message.from_user.mention))
