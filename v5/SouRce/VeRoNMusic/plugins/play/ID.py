import asyncio
import os
import time
import requests
import random
import re
import textwrap
import aiofiles
import aiohttp
import time
import requests
import datetime
import sys
import config
from pyrogram import enums
import asyncio
import aiohttp
import datetime
from pytz import timezone
from pyrogram import filters
from pyrogram import Client
from VeRoNMusic.core.call import KIM
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from VeRoNMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from VeRoNMusic import app
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait

@app.on_message(filters.command(["المالك", "صاحب الخرابه", "المنشي"], ""), group=95)
async def ownner(client: Client, message: Message):
    x = []
    async for m in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
         if m.status == ChatMemberStatus.OWNER:
            x.append(m.user.id)
    if len(x) != 0:        
       m = await app.get_users(int(x[0]))
       if m.photo:
         async for photo in app.get_chat_photos(x[0],limit=1):
          await message.reply_photo(photo.file_id,caption=f"‹ مالك الجروب › ᥫ᭡\n\n𝅄 𓏺 𝖮𝗐𝗇𝖾𝗋 𝖭𝖺𝗆𝖾 : {m.first_name}\n𝅄 𓏺 𝖴𝗌𝖾𝗋 : [@{m.username}]\n𝅄 𓏺 𝖨𝖣 : `{m.id}`\n\n𝅄 𓏺 Chat : `{message.chat.title}`\n𝅄 𓏺 ID Chat : `{message.chat.id}`",reply_markup=InlineKeyboardMarkup(
             [              
               [          
                 InlineKeyboardButton(m.first_name, url=f"https://t.me/{m.username}")
               ],             
             ]                 
            )                     
          )
       else:
        await message.reply_text(f"‹ مالك الجروب › ᥫ᭡\n\n𝅄 𓏺 𝖮𝗐𝗇𝖾𝗋 𝖭𝖺𝗆𝖾 : {m.first_name}\n𝅄 𓏺 𝖴𝗌𝖾𝗋 : [@{m.username}]\n𝅄 𓏺 𝖨𝖣 : `{m.id}`\n\n𝅄 𓏺 Chat : `{message.chat.title}`\n𝅄 𓏺 ID Chat : `{message.chat.id}`", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(m.first_name, url=f"https://t.me/{m.username}")],]))
    else:
        await message.reply_text("المالك غير موجود في المجموعة")

iddof = []
@app.on_message(filters.command(["قفل الايدي", "تعطيل الايدي"], ""), group=509)
async def iddlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7895466915:
      if message.chat.id in iddof:
        return await message.reply_text("الايدي معطل بالفعل")
      iddof.append(message.chat.id)
      return await message.reply_text("تم تعطيل الايدي بنجاح")
   else:
      return await message.reply_text("هذا الامر للمشرفين فقط")

@app.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"], ""), group=678)
async def iddopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7895466915:
      if not message.chat.id in iddof:
        return await message.reply_text("الايدي مفعل بالفعل")
      iddof.remove(message.chat.id)
      return await message.reply_text("تم تفعيل الايدي بنجاح")
   else:
      return await message.reply_text("هذا الامر للمشرفين فقط")

@app.on_message(filters.command(["ايدي","الايدي","ا"], ""), group=99)
async def iddd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo, caption=f"""‹ معلومات العضو › ᥫ᭡\n\n𝅄 𓏺 𝖭𝖺𝗆𝖾 : {message.from_user.mention}\n𝅄 𓏺 𝖴𝗌𝖾𝗋 : [@{message.from_user.username}]\n𝅄 𓏺 𝖨𝖣 : `{message.from_user.id}`\n𝅄 𓏺 Bio : `{usr.bio}`\n\n𝅄 𓏺 Chat : `{message.chat.title}`\n𝅄 𓏺 ID Chat : `{message.chat.id}`""", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )

kashf = []
@app.on_message(filters.command(["قفل كشف", "تعطيل كشف"], ""), group=8888811223330099)
async def iddlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7895466915:
      if message.chat.id in kashf:
        return await message.reply_text("الكشف معطل بالفعل")
      kashf.append(message.chat.id)
      return await message.reply_text("تم تعطيل الكشف بنجاح")
   else:
      return await message.reply_text("هذا الامر للمشرفين فقط")

@app.on_message(filters.command(["فتح كشف", "تفعيل كشف"], ""), group=70000000000000001111)
async def iddopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.chat.id in kashf:
        return await message.reply_text("الكشف مفعل بالفعل")
      kashf.remove(message.chat.id)
      return await message.reply_text("تم تفعيل الكشف بنجاح")
   else:
      return await message.reply_text("هذا الامر للمشرفين فقط")

@app.on_message(filters.command(["كشف","مين دا","الكشف"], ""), group=1024)
async def kassfggg(client, message):
    if message.chat.id in kashf:
      return await message.reply_text("الكشف معطل من قبل الادارة")

    if not message.reply_to_message:
        return await message.reply_text("يجب الرد على المستخدم")    
    user = await client.get_users(message.reply_to_message.from_user.id)
    name = user.first_name
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    chat_username = f"@{message.chat.username}" 
    chat_name = message.chat.title
    username = f"@{message.reply_to_message.from_user.username}"
    
    user_info = await client.get_chat(message.reply_to_message.from_user.id)
    bio = user_info.bio
    
    user_chat = await client.get_chat(message.reply_to_message.from_user.id)
    
    if user_chat.photo:
        photo = await app.download_media(user_chat.photo.big_file_id)
        await message.reply_photo(
            photo=photo,
            caption=f"‹ معلومات العضو › ᥫ᭡\n\n𝅄 𓏺 𝖭𝖺𝗆𝖾 : {message.reply_to_message.from_user.mention}\n𝅄 𓏺 𝖴𝗌𝖾𝗋 : [{username}]\n𝅄 𓏺 𝖨𝖣 : `{user_id}`\n𝅄 𓏺 Bio : `{bio}`\n\n𝅄 𓏺 Chat : `{chat_name}`\n𝅄 𓏺 ID Chat : `{chat_id}``",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(name, url=f"https://t.me/{message.reply_to_message.from_user.username}")]])
        )
    else:
        await message.reply_text(
            f"‹ معلومات العضو › ᥫ᭡\n\n𝅄 𓏺 𝖭𝖺𝗆𝖾 : {message.reply_to_message.from_user.mention}\n𝅄 𓏺 𝖴𝗌𝖾𝗋 : [{username}]\n𝅄 𓏺 𝖨𝖣 : `{user_id}`\n𝅄 𓏺 Bio : `{bio}`\n\n𝅄 𓏺 Chat : `{chat_name}`\n𝅄 𓏺 ID Chat : `{chat_id}``",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(name, url=f"https://t.me/{message.from_user.username}")]])
        )

iddof = []
@app.on_message(filters.command(["قفل جمالي", "تعطيل جمالي"], ""), group=509)
async def iddlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7895466915:
      if message.chat.id in iddof:
        return await message.reply_text("الجمالي معطل بالفعل")
      iddof.append(message.chat.id)
      return await message.reply_text("تم تعطيل الجمالي بنجاح")
   else:
      return await message.reply_text("هذا الامر للمشرفين فقط")

@app.on_message(filters.command(["فتح جمالي", "تفعيل جمالي"], ""), group=678)
async def iddopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7895466915:
      if not message.chat.id in iddof:
        return await message.reply_text("الجمالي مفعل بالفعل")
      iddof.remove(message.chat.id)
      return await message.reply_text("تم تفعيل الجمالي بنجاح")
   else:
      return await message.reply_text("هذا الامر للمشرفين فقط")

@app.on_message(filters.command(["جمالي"], ""), group=104)
async def idjjdd(client, message):
    if message.chat.id in iddof:
      return await message.reply_text("الجمالي معطل من قبل الادارة")
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    i = ["1","10", "15","20", "25","30","35", "40","45", "50","55", "60"," 66", "70","77", "80","85", "90","99", "100","1000" ]
    ik = random.choice(i)
    if usr.photo:
        photo = await app.download_media(usr.photo.big_file_id)
        await message.reply_photo(photo, caption=f"نسبة جمالك هي ({ik})% ❤️", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )    
    else:
        await message.reply_text("يجب أن يكون لديك صورة حساب لاستخدام هذا الأمر")               

tarof = []

@app.on_message(filters.command(["تعطيل الترحيب","قفل الترحيب"], ""), group=888888888888888811234)
async def disable_welcome(client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7895466915:
        if message.chat.id in tarof:
            return await message.reply_text("الترحيب معطل بالفعل")
        tarof.append(message.chat.id)
        return await message.reply_text("تم تعطيل الترحيب بنجاح")
    else:
        return await message.reply_text("هذا الامر للمشرفين فقط")

@app.on_message(filters.command(["تفعيل الترحيب","فتح الترحيب"], ""), group=6666666666123090000011)
async def enable_welcome(client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7895466915:
        if message.chat.id not in tarof:
            return await message.reply_text("الترحيب مفعل بالفعل")
        tarof.remove(message.chat.id)
        return await message.reply_text("تم تفعيل الترحيب بنجاح")
    else:
        return await message.reply_text("هذا الامر للمشرفين فقط")

@app.on_message(filters.new_chat_members, group=554)
async def welcome(client: Client, message: Message):
    if message.chat.id in tarof:
        return await message.reply_text("الترحيب معطل من قبل الادارة")
    usr = await client.get_chat_member(message.chat.id, message.from_user.id)
    if usr.status != "kicked":
        chat_id = message.chat.id
        keyboard = [
            [InlineKeyboardButton(
                message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
            ]
        ]
        await app.send_message(
            chat_id=chat_id,
            text=f"مرحباً بك في المجموعة\nالاسم: {message.from_user.mention}\nالمعرف: @{message.from_user.username}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

@app.on_message(filters.left_chat_member, group=222307)
async def send_leave_message(client: Client, message: Message):
    try:
        usr = await client.get_chat(message.from_user.id)
        name = usr.first_name
        chat_id = message.chat.id
        await app.send_message(chat_id=chat_id, text=f"غادر المجموعة\nالاسم: {message.from_user.mention}\nالمعرف: @{message.from_user.username}")
    except Exception as e:
        print(f"حدث خطأ أثناء مغادرة العضو: {str(e)}")

@app.on_message(filters.command(["الجروب", "جروب","انا فين"], ""), group=666)
async def ginnj(client: Client, message: Message):
    chat_idd = message.chat.id
    chat_name = message.chat.title
    msg = await message.reply("جاري التحميل...")
    import asyncio
    await asyncio.sleep(2)
    await msg.delete()
    chat_username = f"@{message.chat.username}"
    if message.chat.photo:
        photo = await client.download_media(message.chat.photo.big_file_id)
        await message.reply_photo(
        photo=photo,
        caption=f"""معلومات المجموعة:
اسم المجموعة: {chat_name}
ايدي المجموعة: `{chat_idd}`
رابط المجموعة: {chat_username}""",     
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            chat_name, url=f"https://t.me/{message.chat.username}")
                    ],
                ]
            ),
        )
    else:
        await message.reply_text(f"""معلومات المجموعة:
اسم المجموعة: {chat_name}
ايدي المجموعة: `{chat_idd}`
رابط المجموعة: {chat_username}""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(chat_name, url=f"https://t.me/{message.chat.username}")],]))


@app.on_message(filters.command(["اسمي"], ""), group=6658)
async def vgdg(client: Client, message: Message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    await message.reply_text(
        f"""اسمك هو: `{message.from_user.mention}`""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )