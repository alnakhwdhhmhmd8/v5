from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os


from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from pyrogram import filters, Client
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import *
from pyrogram import enums
from typing import Union, List, Iterable
from datetime import datetime
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import ChatPermissions, ChatPrivileges
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
import sys
from pyrogram import Client as client
from pyrogram.errors import FloodWait
from pyrogram import Client, idle
from random import randint
from pyrogram.enums import ChatType
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from config import *
from random import choice
from telegraph import upload_file
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton as Button, InlineKeyboardMarkup as Markup

import asyncio
import string
import os
import time
import requests
from pyrogram import filters
import random
import aiohttp
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from VeRoNMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from VeRoNMusic import app
from random import  choice, randint
from pytube import Search
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from VeRoNMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from VeRoNMusic import app
import requests
import pyrogram
from VeRoNMusic.misc import SUDOERS
from pyrogram import Client, emoji 
from config import*
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import MessageNotModified
 
 

 
from pyrogram import Client, filters
import random

# Constants for message typesئhms = {}

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

hmses = {}
waiting_for_hms = False
hms_ids = ""


@app.on_message(filters.reply & filters.regex("همسه") & filters.group, group=5765357)
async def reply_with_link(client, message):
    bot_username = (await client.get_me()).username
    user_id = message.reply_to_message.from_user.id
    my_id = message.from_user.id
    bar_id = message.chat.id
    start_link = f"https://t.me/{bot_username}?start=hms{my_id}to{user_id}in{bar_id}"
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("اضغط لإرسال الهمسه!", url=start_link)]
        ]
    )  
    await message.reply_text("إضغط لإرسال همسه!", reply_markup=reply_markup)

@app.on_message(filters.command("start"), group=5790)
async def hms_start(client, message): 
    global waiting_for_hms, hms_ids
    bot_username = (await client.get_me()).username
    if len(message.command) > 1 and message.command[1].startswith("hms"):
        hms_ids = message.command[1]
        waiting_for_hms = True
        await message.reply_text(
            "-> أرسل الهمسه الآن.\n√", 
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("إلغاء ❌️", callback_data="hms_cancel")
            ]])
        )

@app.on_message(filters.private & filters.text & ~filters.command("start"), group=576)
async def send_hms(client, message): 
    global waiting_for_hms, hms_ids
    if waiting_for_hms:    
        try:
            to_id = int(hms_ids.split("to")[-1].split("in")[0])
            from_id = int(hms_ids.split("hms")[-1].split("to")[0])
            in_id = int(hms_ids.split("in")[-1])
            
            user = await client.get_users(to_id)
            hmses[str(to_id)] = {"hms": message.text, "bar": in_id}
            
            await message.reply_text("-> تم ارسال الهمسه.\n√")
            await client.send_message(
                chat_id=in_id,
                text=f"<blockquote><b>ılıı◁❚ ✘ᴠᴇʀᴏɴ✘ ❚▷ıılı\n╮❖ لديك همسه جديده\n╯❖ انت فقط من يستطيع رؤيتها [{user.mention}]</b></blockquote>",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("اضغط لرؤية الهمسه 🥺", callback_data="hms_answer")],
                    [InlineKeyboardButton("ᴠᴇʀᴏɴ", url=SUPPORT_CHANNEL)]
                ])
            )
        except Exception as e:
            await message.reply_text(f"حدث خطأ: {e}")
        finally:
            waiting_for_hms = False
  
@app.on_callback_query(filters.regex("hms_answer"), group=888890)
async def display_hms(client, callback):  
    in_id = callback.message.chat.id
    who_id = callback.from_user.id  
    if str(who_id) in hmses and hmses[str(who_id)]["bar"] == in_id:
        await callback.answer(hmses[str(who_id)]["hms"], show_alert=True)
    else:
        await callback.answer("هذه الهمسه ليست لك!", show_alert=True)
    
@app.on_callback_query(filters.regex("hms_cancel"), group=769800)
async def cancel_hms(client, callback):  
    global waiting_for_hms
    waiting_for_hms = False  
    await callback.message.edit_text("-> تم إلغاء الهمسه!\n√")
