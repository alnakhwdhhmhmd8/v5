from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from VeRoNMusic import app
from VeRoNMusic.core.call import KIM
from VeRoNMusic.utils.database.memorydatabase import is_muted, mute_off, mute_on
from VeRoNMusic.utils.decorators import AdminRightsCheck


@app.on_message(filters.command(["vcmute"], "") & filters.channel)
@AdminRightsCheck
async def mute_admin(cli, message: Message, _, chat_id):
    _ = get_string("en")
    if await is_muted(message.chat.id):
        return await message.reply_text(_["admin_5"], disable_web_page_preview=True)
    await mute_on(message.chat.id)
    await KIM.mute_stream(message.chat.id)
    await message.reply_text(
        _["admin_6"].format(message.chat.title), disable_web_page_preview=True
    )


@app.on_message(filters.command(["vcunmute"], "") & filters.channel)
@AdminRightsCheck
async def unmute_admin(Client, message: Message, _, chat_id):
    _ = get_string("en")
    if not await is_muted(message.chat.id):
        return await message.reply_text(_["admin_7"], disable_web_page_preview=True)
    await mute_off(message.chat.id)
    await KIM.unmute_stream(message.chat.id)
    await message.reply_text(
        _["admin_8"].format(message.chat.title), disable_web_page_preview=True
    )




@app.on_message(filters.command(["vcmute"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def mute_admin(cli, message: Message, _, chat_id):
    if await is_muted(message.chat.id):
        return await message.reply_text(_["admin_5"], disable_web_page_preview=True)
    await mute_on(message.chat.id)
    await KIM.mute_stream(message.chat.id)
    await message.reply_text(
        _["admin_6"].format(message.from_user.mention), disable_web_page_preview=True
    )


@app.on_message(filters.command(["vcunmute"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def unmute_admin(Client, message: Message, _, chat_id):
    if not await is_muted(message.chat.id):
        return await message.reply_text(_["admin_7"], disable_web_page_preview=True)
    await mute_off(message.chat.id)
    await KIM.unmute_stream(message.chat.id)
    await message.reply_text(
        _["admin_8"].format(message.from_user.mention), disable_web_page_preview=True
    )



