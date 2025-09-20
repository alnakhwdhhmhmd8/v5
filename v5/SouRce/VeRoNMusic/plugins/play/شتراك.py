import asyncio
import os
from VeRoNMusic.misc import SUDOERS
import re
from collections import defaultdict
from pyrogram import filters, Client
from pyrogram.enums import *
from pyrogram.errors import *
from VeRoNMusic import *
from config import *
from pyrogram.types import *
import asyncio
from pyromod import listen
from config import OWNER_ID
from pyrogram import *
from dotenv import load_dotenv
from os import getenv
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from pyrogram import Client, emoji, filters
from pyrogram.types import Message
from pyrogram.errors import MessageNotModified
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import CallbackQuery, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from VeRoNMusic import app
from pyrogram import Client, filters
from pyrogram.types import *
from pyrogram.errors import PeerIdInvalid
from pyrogram.errors import UserNotParticipant

from os import getenv
from dotenv import load_dotenv

load_dotenv()


def is_owner(_, __, message):
    return message.from_user.id == OWNER_ID

join_locked = False   
ch = ""

@app.on_message(filters.regex("تفعيل الاشتراك"), group=501828)
async def lock_joiiin(client, message):
    global ch
    ask = await app.ask(message.chat.id, f"**تاكد من رفع البوت مشرف في القناه \n وارسل معرف القناه بدون @**", timeout=300)
    ch = ask.text 
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    global join_locked
    join_locked = True
    await message.reply_text(f"تم تفعيل الاشتراك الجروبات بنجاح")

@app.on_message(filters.regex("تعطيل اشتراك"), group=501854444477728)
async def unlock_joinn(client, message):
    global join_locked
    join_locked = False
    await message.reply_text(f"تم تعطيل الاشتراك الجروبات بنجاح")

@app.on_message(filters.group & filters.text & filters.create(lambda _, __, message: join_locked), group=50180113452128)
async def check_subscription(client, message):
    global ch
    try:
        usr = await client.get_chat(message.from_user.id)
        name = usr.first_name
        user_id = usr.id
        
        # التحقق من الاشتراك
        await client.get_chat_member(ch, user_id)
        
    except UserNotParticipant:
        # إنشاء زر اشتراك مع منشن للمستخدم
        mention_link = f"[{name}](tg://user?id={user_id})"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("اشتراك هنا", url=f"https://t.me/{ch}")]
        ])
        
        # إرسال الرسالة مع المنشن
        await app.send_message(
            chat_id=message.chat.id,
            text=f"**{mention_link} عزيزي، عليك الاشتراك في القناة أولاً 🚀**\nاشترك ثم أعد المحاولة!",
            reply_markup=keyboard,
            parse_mode=ParseMode.MARKDOWN
        )
        await message.delete()
        return
    except Exception as e:
        print(f"Error: {e}")
    
    message.continue_propagation()