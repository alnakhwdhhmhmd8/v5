from pyrogram import Client
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
import os
from VeRoNMusic import app

import asyncio
import aiohttp
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram import enums
import config

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from VeRoNMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from VeRoNMusic import app
from random import  choice, randint

from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton

from pyrogram.enums import ChatMemberStatus, ParseMode
from pyrogram.enums import ParseMode


def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj
                




@app.on_message(filters.command(["المطور", "مطور","مطور البوت"], ""), group=5006721136) 
async def dev(client: Client, message: Message):
     bot_username = client.me.username
     user = await client.get_chat(OWNER_ID)
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     photo = user.photo.big_file_id
     photo = await client.download_media(photo)
     link = f"https://t.me/{message.chat.username}"
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"**╭❖ɴᴀᴍᴇ: {message.from_user.mention} \n│᚜❖  ᴄʜᴀᴛ ɴᴀᴍᴇ: {title}" if message.from_user else f"╰❖ ᚐᴄʜᴀᴛ ɴᴀᴍᴇ: {message.chat.title}**"
     try:
      await client.send_message(username, f"**<b>[سوࢪس فيࢪوטּ | 𝙎𝙤𝙪𝙧𝙘𝙚 𝙑𝙚𝙧𝙤𝙣. #]</b>\nحبي في حد بينادي عليك\n{chat_title}\n╰❖ ᚐᴄʜᴀᴛ ɪᴅ : {message.chat.id}**",
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
     except:
        pass
     await message.reply_photo(
     photo=photo,
     caption=f"**<b>[سوࢪس فيࢪوטּ | 𝙎𝙤𝙪𝙧𝙘𝙚 𝙑𝙚𝙧𝙤𝙣. #]</b>\n\n╭❖ᴅᴇᴠᚐɴᴀᴍᴇ: {name}\n│᚜❖ᴅᴇᴠᚐᴜꜱᴇʀ : @{username}\n╰❖ᚐʙɪᴏ{bio}**",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
     try:
       os.remove(photo)
     except:
        pass
        
        
        

@app.on_message(filters.command(["فيرون"], ""), group=84444677721136)
async def yas(client, message):
    usr = await client.get_chat("ToxVe")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**<b>[سوࢪس فيࢪوטּ | 𝙎𝙤𝙪𝙧𝙘𝙚 𝙑𝙚𝙧𝙤𝙣. #]</b>\n\n╭❖ᚐɴᴀᴍᴇᚐ: {name}\n│᚜❖ᚐᴜꜱᴇʀ: @{usr.username}\n│᚜❖ᚐɪᴅᚐ: `{usr.id}`\n╰❖ᚐʙɪᴏᚐ: {usr.bio}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )