from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from pyrogram.types import Message
from VeRoNMusic import app
from config import OWNER_ID
import json
import os
import asyncio
import platform
import re
import socket
import uuid
import os
import speedtest
import asyncio
import platform
import asyncio

import time
import requests
from sys import version as pyver
from datetime import datetime

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid, FloodWait
from pyrogram.types import CallbackQuery, InputMediaPhoto, Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from pytgcalls.__version__ import __version__ as pytgver

import config
from config import OWNER_ID
from VeRoNMusic import YouTube, app
from VeRoNMusic import app as Client
from VeRoNMusic.core.userbot import assistants
from VeRoNMusic.misc import SUDOERS, pymongodb
from VeRoNMusic.plugins import ALL_MODULES

from VeRoNMusic.utils.decorators.language import language, languageCB
from VeRoNMusic.utils.inline.stats import back_stats_buttons, stats_buttons


import asyncio
from pyrogram import Client, filters
from strings import get_command
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from VeRoNMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


from pyrogram import filters
import random
from pyrogram import enums
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from VeRoNMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from VeRoNMusic import app
from random import  choice, randint


loop = asyncio.get_running_loop()

# Commands

def is_owner(_, __, message):

    return message.from_user.id == OWNER_ID



# كيبورد المطور المحدث
REPLY_MESSAGE_OWNER = "**مرحبا عزيزي المطور**"
REPLY_MESSAGE_BUTTONS_OWNER = [
    [("الاحصيات")],
    [("تعين اشتراك"), ("الغاء اشتراك")],
    [("تعين اسم البوت")],
    [("تفعيل التواصل"), ("تعطيل التواصل")],            
    [("اذاعه"), ("اذاعه بالتوجيه"), ("اذاعه بالتثبيت")],
    [("جلب نسخه"), ("رفع نسخه")],
    [("اخفاء الكيبورد")],
    [("الغاء")]
]

@app.on_message(filters.command("^/start"), group=48384838383)
async def owner_start(client, message: Message):
    if message.from_user.id == OWNER_ID:
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS_OWNER, resize_keyboard=True, selective=True)
        await message.reply(
            text=REPLY_MESSAGE_OWNER,
            reply_markup=reply_markup
        )

# ----------------------------------- الإحصائيات -----------------------------------
@app.on_message(filters.command(["الاحصيات"], ""), group=743884383848)
async def stats_handler(client, message):
    stats_text = await generate_stats()
    await message.reply(stats_text)

async def generate_stats():
    try:
        # جلب الإحصائيات من قاعدة البيانات
        total_users = await pymongodb.total_users()
        all_chats = await pymongodb.get_all_chats()
        
        # تصنيف الدردشات
        groups = 0
        channels = 0
        supergroups = 0
        
        for chat in all_chats:
            if chat['type'] == 'group':
                groups += 1
            elif chat['type'] == 'channel':
                channels += 1
            elif chat['type'] == 'supergroup':
                supergroups += 1
                
        # معلومات النظام
        system_info = f"""
📊 الاحصائيات التفصيلية:

👤 المستخدمين الفرديين: {total_users}
👥 المجموعات العادية: {groups}
🗣 المجموعات الخارقة: {supergroups}
📡 القنوات: {channels}
🔄 إجمالي الدردشات: {len(all_chats)}

📚 إصدارات المكتبات:
• Pyrogram: {pyrover}
• Py-TgCalls: {pytgver}
        """
        
        return system_info
        
    except Exception as e:
        return f"⚠️ حدث خطأ في جلب الإحصائيات: {str(e)}"
        
# ---------------------------- نظام الاشتراك الإجباري ----------------------------
@app.on_message(filters.command(["تعين اشتراك"], ""), group=48385838484)
async def set_force_sub(client, message):
    try:
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            return await message.reply("❗ يرجى إرسال معرف القناة بعد الأمر (مثال: @ChannelName)")
        
        channel = args[1].strip()
        await pymongodb.update_force_sub(channel)
        await message.reply(f"✓ تم تعيين القناة {channel} كاشتراك إجباري")
    except Exception as e:
        await message.reply(f"❌ خطأ: {str(e)}")

@app.on_message(filters.command(["الغاء اشتراك"], ""))
async def remove_force_sub(client, message):
    await pymongodb.remove_force_sub()
    await message.reply("✓ تم إلغاء الاشتراك الإجباري")

# ---------------------------- نظام التواصل ----------------------------
@app.on_message(filters.command(["تفعيل التواصل"], ""), group=74838438488)
async def enable_communication(client, message):
    await pymongodb.toggle_communication(True)
    await message.reply("✓ تم تفعيل نظام التواصل")

@app.on_message(filters.command(["تعطيل التواصل"], ""))
async def disable_communication(client, message):
    await pymongodb.toggle_communication(False)
    await message.reply("✓ تم تعطيل نظام التواصل")

# ---------------------------- نظام الإذاعة ----------------------------
async def broadcast_users(client, message, broadcast_type):
    users = await pymongodb.get_all_users()
    success = 0
    failed = 0
    
    msg = await message.reply("♻️ جاري بدء الإذاعة...")
    
    for user_id in users:
        try:
            if broadcast_type == "normal":
                await message.reply_to_message.copy(user_id)
            elif broadcast_type == "forward":
                await client.forward_messages(user_id, message.chat.id, message.reply_to_message.id)
            elif broadcast_type == "pin":
                sent_msg = await message.reply_to_message.copy(user_id)
                await sent_msg.pin()
            
            success += 1
            await asyncio.sleep(0.2)
        except Exception as e:
            failed += 1
    
    await msg.edit(f"""
✅ الإذاعة اكتملت
✓ الناجحة: {success}
✗ الفاشلة: {failed}
    """)

@app.on_message(filters.command(["اذاعه"], ""), group=84844884848)
async def normal_broadcast(client, message):
    if not message.reply_to_message:
        return await message.reply("❗ يرجى الرد على الرسالة المراد إذاعتها")
    await broadcast_users(client, message, "normal")

@app.on_message(filters.command(["اذاعه بالتوجيه"], ""), group=488485485848)
async def forward_broadcast(client, message):
    if not message.reply_to_message:
        return await message.reply("❗ يرجى الرد على الرسالة المراد توجيهها")
    await broadcast_users(client, message, "forward")

@app.on_message(filters.command(["اذاعه بالتثبيت"], ""))
async def pin_broadcast(client, message):
    if not message.reply_to_message:
        return await message.reply("❗ يرجى الرد على الرسالة المراد إذاعتها")
    await broadcast_users(client, message, "pin")

# ---------------------------- النسخ الاحتياطي ----------------------------
@app.on_message(filters.command(["جلب نسخه"], ""))
async def backup_data(client, message):
    try:
        backup = await pymongodb.get_full_backup()
        
        with open("VeronBackup.json", "w") as f:
            json.dump(backup, f, indent=4)
        
        await client.send_document(
            message.chat.id,
            "VeronBackup.json",
            caption="♻️ النسخة الاحتياطية للبوت"
        )
        os.remove("VeronBackup.json")
    except Exception as e:
        await message.reply(f"❌ خطأ في النسخ الاحتياطي: {str(e)}")

@app.on_message(filters.command(["رفع نسخه"], ""))
async def restore_data(client, message):
    try:
        if not message.document:
            return await message.reply("❗ يرجى إرسال ملف النسخة الاحتياطية")
        
        file_path = await message.download()
        
        with open(file_path, "r") as f:
            backup = json.load(f)
        
        await pymongodb.restore_backup(backup)
        await message.reply("✓ تم استعادة النسخة الاحتياطية بنجاح")
        os.remove(file_path)
    except Exception as e:
        await message.reply(f"❌ خطأ في الاستعادة: {str(e)}")

# ---------------------------- التحكم بالكيبورد ----------------------------
@app.on_message(filters.command(["اخفاء الكيبورد"], ""))
async def hide_keyboard(client, message):
    await message.reply(
        "✓ تم إخفاء الكيبورد",
        reply_markup=ReplyKeyboardRemove()
    )

@app.on_message(filters.command(["الغاء"], ""))
async def cancel_action(client, message):
    await message.reply(
        "✓ تم الإلغاء",
        reply_markup=ReplyKeyboardRemove()
    )

# ---------------------------- التحقق من الاشتراك ----------------------------
@app.on_message(filters.command("start") & filters.private)
async def force_sub_check(client, message):
    force_sub = await pymongodb.get_force_sub()
    if not force_sub:
        return await normal_start(client, message)
    
    try:
        member = await client.get_chat_member(force_sub, message.from_user.id)
        if member.status not in ["member", "administrator", "creator"]:
            raise Exception("Not member")
    except Exception:
        return await message.reply(
            f"⛔ عليك الانضمام للقناة أولاً:\n{force_sub}",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("انضمام للقناة", url=f"t.me/{force_sub[1:]}")
            ]])
        )
    
    await normal_start(client, message)

async def normal_start(client, message):
    await message.reply(
        "مرحبا بك في بوت فيرون ميوزك!",
        reply_markup=ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True)
    )