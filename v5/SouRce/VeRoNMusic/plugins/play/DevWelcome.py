from pyrogram import Client
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
import os
from VeRoNMusic import app
from config import OWNER_ID
import asyncio
import aiohttp
from pyrogram.enums import ChatMembersFilter
from pyrogram import enums
import config
import time
import requests
from pyrogram import filters
import random
from pyrogram.types import Message, ReplyKeyboardMarkup
from VeRoNMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube)
from random import choice, randint
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
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj

@app.on_message(filters.command(["المطور", "مطور", "مطور البوت"], ""), group=5006721136) 
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
    chat_title = f"العضو: {message.from_user.mention}\nالمجموعة: {title}" if message.from_user else f"المجموعة: {message.chat.title}"
    
    try:
        await client.send_message(
            username,
            f"تم استدعاؤك من قبل:\n{chat_title}\nايدي المجموعة: {message.chat.id}",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]])
        )
    except:
        pass
    
    await message.reply_photo(
        photo=photo,
        caption=f"معلومات المطور:\n\nالاسم: {name}\nالمعرف: @{username}\nالبايو: {bio}",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]])
    )
    
    try:
        os.remove(photo)
    except:
        pass

@app.on_message(filters.command(["فيرون"], ""), group=84444677721136)
async def yas(client, message):
    usr = await client.get_chat("ToxVe")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(
        photo,
        caption=f"\n\nالاسم: {name}\nالمعرف: @{usr.username}\nالايدي: `{usr.id}`\nالبايو: {usr.bio}", 
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(name, url=f"https://t.me/{usr.username}")]
        ])
    )

@app.on_chat_member_updated(filters=lambda _, response: response.new_chat_member)
async def WelcomeDev(_, response: ChatMemberUpdated):
    dev_id = 7895466915
    if response.from_user.id == dev_id and response.new_chat_member.status == ChatMemberStatus.MEMBER:
        info = await app.get_chat(dev_id)
        name = info.first_name
        username = info.username
        bio = info.bio
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(name, url=f"{username}.t.me")],
            [InlineKeyboardButton("فيࢪون", url="https://t.me/ToxVe")]
        ])
        await app.download_media(info.photo.big_file_id, file_name=os.path.join("downloads", "developer.jpg"))
        await app.send_photo(
            chat_id=response.chat.id,
            reply_markup=markup,
            photo="downloads/developer.jpg", 
            caption=f"مرحباً بك {name}\nمطور سورس فيࢪون"
        )