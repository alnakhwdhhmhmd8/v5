import asyncio
import requests
from VeRoNMusic import app
from VeRoNMusic.core.call import KIM
from VeRoNMusic.utils.database import set_loop
from VeRoNMusic.utils.decorators import AdminRightsCheck
from datetime import datetime
from config import BANNED_USERS, MONGO_DB_URI, OWNER_ID
from VeRoNMusic.utils import bot_sys_stats
from VeRoNMusic.utils.decorators.language import language
import random
import time
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from aiohttp import ClientSession
from traceback import format_exc
import config
import re
import string
import lyricsgenius as lg
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
from pyrogram import Client, filters
from VeRoNMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
import sys
import os
from pyrogram.types import ChatPermissions, ChatPrivileges
from pyrogram.errors import PeerIdInvalid
from os import getenv
from VeRoNMusic.misc import SUDOERS
from pyrogram import filters, Client
from telegraph import upload_file
from dotenv import load_dotenv


from VeRoNMusic import app
unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)

mute_permission = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False, 
    can_send_other_messages=False,
    can_send_polls=False,
    can_add_web_page_previews=False,
    can_change_info=False,
    can_pin_messages=False,
    can_invite_users=True,
)
# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂[التقيد]▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂

muttof = []
@app.on_message(filters.command(["قفل التقيد", "تعطيل التقيد"], ""), group=419)
async def muttlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7728230165:
      if message.chat.id in muttof:
        return await message.reply_text("تم قفل التقيد من قبل ✨")
      muttof.append(message.chat.id)
      return await message.reply_text("تم تعطيل التقيد بنجاح ✨")
   else:
      return await message.reply_text("هذا الامر ليس لك ✨")

@app.on_message(filters.command(["فتح التقيد", "تفعيل التقيد"], ""), group=424)
async def muttopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7728230165:
      if not message.chat.id in muttof:
        return await message.reply_text("التقيد مفعل من قبل ✨")
      muttof.remove(message.chat.id)
      return await message.reply_text("تم فتح التقيد بنجاح ✨")
   else:
      return await message.reply_text("هذا الامر ليس لك ✨")
        
        
@app.on_message(filters.command(["الغاء تقيد","الغاء التقيد"], ""), group=94) 
async def mute(client: Client, message: Message):
   global restricted_users
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7728230165:
    if message.chat.id in muttof:
      return   	   	
    await app.restrict_chat_member(
                       chat_id=message.chat.id,
                       user_id=message.reply_to_message.from_user.id,
                       permissions=unmute_permissions,
                   )
    await app.send_message(message.chat.id, f"تم الغاء تقيد {message.reply_to_message.from_user.mention} بنجاح ✨")
   else:
         await message.reply_text(f"هذا الامر ليس لك ✨")


restricted_users = []
@app.on_message(filters.command(["تقيد"], ""), group=62)
async def mute(client: Client, message: Message):
    global restricted_users
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7728230165:
        if message.chat.id in muttof:
            return
        if message.reply_to_message.from_user.id == 7728230165:
            await app.send_message(message.chat.id, "لا يمكن تقيد المطور فيࢪون ✨")
        else:
            mute_permission = ChatPermissions(can_send_messages=False)
            await app.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                permissions=mute_permission,
            )
            restricted_user = message.reply_to_message.from_user
            restricted_users.append(restricted_user)
            await app.send_message(message.chat.id, f"تم تقيد {restricted_user.mention} بنجاح ✨")
    else:
         await message.reply_text(f"هذا الامر ليس لك ✨")




@app.on_message(filters.command(["مسح المقيدين"], ""), group=40)
async def unmute(client: Client, message: Message):
    global restricted_users
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER] or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
        count = len(restricted_users)
        for user in restricted_users:
            await client.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=user.id,
                permissions=unmute_permissions,
            )
        restricted_users = []
        await message.reply_text(f"تم مسح {count} من المقيدين بنجاح ✨")
    else:
        await message.reply_text(f"هذا الامر ليس لك ✨")
    

@app.on_message(filters.command(["المقيدين"], ""), group=13100920)
async def get_restr_users(client: Client, message: Message):
    global restricted_users
    count = len(restricted_users)
    X = 0
    user_ids = [str(user.id) for user in restricted_users]
    response = f"قائمة المقيدين وعددهم: {count}\n"
    response += "[سوࢪس فيࢪوטּ | 𝙎𝙤𝙪𝙧𝙘𝙚 𝙑𝙚𝙧𝙤𝙣. #]\n"
    response += "\n".join(f"{X+i+1}. {user_id}" for i, user_id in enumerate(user_ids))
    await message.reply_text(response)


# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂[الحظر]▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂

gaaof = []
@app.on_message(filters.command(["تعطيل الحظر", "تعطيل الطرد"], ""), group=504)
async def gaalock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in gaaof:
        return await message.reply_text("الامر معطل من قبل ✨")
      gaaof.append(message.chat.id)
      return await message.reply_text("تم تعطيل الحظر بنجاح ✨")
   else:
      return await message.reply_text("هذا الامر ليس لك ✨")

@app.on_message(filters.command(["فتح الطرد", "تفعيل الطرد", "تفعيل الحظر"], ""), group=412)
async def gaaopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.chat.id in gaaof:
        return await message.reply_text("الحظر مفعل من قبل ✨")
      gaaof.remove(message.chat.id)
      return await message.reply_text("تم فتح الطرد و الحظر بنجاح ✨")
   else:
      return await message.reply_text("هذا الامر ليس لك ✨")


        
banned_users = []
@app.on_message(filters.command(["حظر"], ""), group=39)
async def mute(client: Client, message: Message):
   global banned_users    
   chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
   usr = await client.get_chat(message.from_user.id)
   name = usr.first_name
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7728230165:
    if message.chat.id in gaaof:
        return
    if message.reply_to_message.from_user.id == 7728230165:
        await app.send_message(message.chat.id, "ايش تسوي انت هذا فيرون مطور السورس ✨")
    else:
        banned_user = message.reply_to_message.from_user
        banned_users.append(banned_user)
        await app.ban_chat_member(message.chat.id, banned_user.id)
        await app.send_message(message.chat.id, f"تم حظر {banned_user.mention} بنجاح ✨")
   else:
         await message.reply_text(f"هذا الامر ليس لك ✨")

@app.on_message(filters.command(["مسح المحظورين"], ""), group=19)
async def unban_all(client: Client, message: Message):
   usr = await client.get_chat(message.from_user.id)
   usr = await client.get_chat(message.from_user.id)
   name = usr.first_name
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7728230165:
    global banned_users
    count = len(banned_users)
    chat_id = message.chat.id
    failed_count = 0

    for member in banned_users.copy():
        user_id = member.id
        try:
            await client.unban_chat_member(chat_id, user_id)
            banned_users.remove(member)
        except Exception:
            failed_count += 1

    successful_count = count - failed_count

    if successful_count > 0:
        await message.reply_text(f"تم رفع الحظر عن {successful_count} من المحظورين ✨")
    else:
        await message.reply_text("لا يوجد مستخدمين محظورين علشان امسحهم ✨")

    if failed_count > 0:
        await message.reply_text(f"اسف✨ \nفشل في رفع الحظر عن {failed_count} من المحظورين ✨")
   else:
         await message.reply_text(f"هذا الامر ليس لك ✨")
      
                
        
@app.on_message(filters.command(["الغاء حظر","/unban"], ""), group=42)
async def unmutegy(client: Client, message: Message):
    global banned_users
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER] or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
        if not message.reply_to_message:
            return await message.reply_text("يجب الرد على الشخص الذي تريد إلغاء حظره")
        user = message.reply_to_message.from_user
        await app.unban_chat_member(message.chat.id, user.id)
        banned_users.remove(user)
        await app.send_message(message.chat.id, f"تـم الغاء الحظر عن {user.mention} بنجاح ✨")
        


@app.on_message(filters.command(["المحظورين"], ""), group=17389336)
async def get_restricted_users(client: Client, message: Message):
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7728230165:
         global banned_users
         count = len(banned_users)
         user_ids = [str(user.id) for user in banned_users]
         response = f" <u>قائمة المحظورين وعددهم :</u> {count}\n"
         response += "[سوࢪس فيࢪوטּ | 𝙎𝙤𝙪𝙧𝙘𝙚 𝙑𝙚𝙧𝙤𝙣. #]\n"
         response += "\n".join(user_ids)
         await message.reply_text(response)
    else:
        await message.reply_text(f"هذا الامر ليس لك ✨")


from datetime import datetime, timedelta
import asyncio

temp_muted_users = {}

async def restrict_user(client, chat_id, user_id, until_date=None):
    permissions = ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_polls=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False,
        can_change_info=False,
        can_invite_users=False,
        can_pin_messages=False
    )
    await client.restrict_chat_member(
        chat_id=chat_id,
        user_id=user_id,
        permissions=permissions,
        until_date=until_date
    )

@app.on_message(filters.command(["كتم"], prefixes=""), group=39)
async def temp_mute_user(client, message):
    try:
        chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
        if chat_member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and message.from_user.id != 7728230165:
            await message.reply_text("⚠️ هذا الأمر متاح فقط للمشرفين!")
            return
        if not message.reply_to_message:
            await message.reply_text("↩️ يرجى الرد على الشخص المراد كتمه")
            return
        user = message.reply_to_message.from_user
        user_id = user.id
        user_mention = user.mention
        if user_id == 7728230165:
            await message.reply_text("⛔ لا يمكن كتم المطور!")
            return
        command_parts = message.text.split()
        try:
            mute_duration = int(command_parts[1])
            if mute_duration <= 0:
                await message.reply_text("🚫 المدة يجب أن تكون أكبر من الصفر!")
                return
            mute_until = datetime.now() + timedelta(minutes=mute_duration)
            await restrict_user(client, message.chat.id, user_id, mute_until)            
            temp_muted_users[user_id] = mute_until
            await message.reply_text(
                f"⏳ تم كتم {user_mention} لمدة {mute_duration} دقيقة.\n"
                f"⏰ سينتهي الكتم في {mute_until.strftime('%Y-%m-%d %H:%M:%S')}"
            )
            async def unmute_after_duration():
                await asyncio.sleep(mute_duration * 60)
                default_permissions = ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_polls=True,
                    can_send_other_messages=True,
                    can_add_web_page_previews=True,
                    can_change_info=False,
                    can_invite_users=False,
                    can_pin_messages=False
                )
                await client.restrict_chat_member(
                    chat_id=message.chat.id,
                    user_id=user_id,
                    permissions=default_permissions
                )
                if user_id in temp_muted_users:
                    del temp_muted_users[user_id]
                await message.reply_text(f"🔊 تم إلغاء كتم {user_mention} بعد انتهاء المدة")
            asyncio.create_task(unmute_after_duration())
        except ValueError:
            await message.reply_text("❌ المدة يجب أن تكون رقماً صحيحاً!")
    except Exception as e:
        pass
# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂[الكتم]▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂

muted_users = []
@app.on_message(filters.command(["كتم"], ""), group=455667775539)
async def mute_user(client, message):
    global muted_users    
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7728230165:    
        if message.reply_to_message.from_user.id == 7728230165:
            await app.send_message(message.chat.id, "عذرا لا يمكنك كتم المطور فيࢪون")
        else:	
         if message.reply_to_message:
           user_id = message.reply_to_message.from_user.mention
         if user_id not in muted_users:
            muted_users.append(user_id)
            await message.reply_text(f"تم كتم {user_id} لي سوء سلوكه ✨")
         else:
           await message.reply_text(f"في حد كتم {user_id} قبلك لي سوء سلوكه ✨")
    else:
        await message.reply_text(f"هذا الامر ليس لك ✨")


@app.on_message(filters.command(["الغاء الكتم"], ""), group=62)
async def unmute_user(client, message):
   global muted_users
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7728230165:	
    user_id = message.reply_to_message.from_user.mention
    if user_id in muted_users:
        muted_users.remove(user_id)
        await message.reply_text(f"تم الغاء كتم {user_id} بشرط تحسين سلوكه ✨")
   else:
        await message.reply_text(f"هذا الامر ليس لك ✨")    
       
        
        
       
@app.on_message(filters.text)
async def handle_message(client, message):
    if message.from_user and message.from_user.mention in muted_users:
        await client.delete_messages(chat_id=message.chat.id, message_ids=message.id)

@app.on_message(filters.command(["المكتومين"], ""), group=137)
async def get_rmuted_users(client, message):
    global muted_users
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7728230165:
         count = len(muted_users)
         user_ids = [str(user) for user in muted_users]
         response = f" <u>قائمة المكتومين وعددهم :</u> {count}\n"
         response += "[سوࢪس فيࢪوטּ | 𝙎𝙤𝙪𝙧𝙘𝙚 𝙑𝙚𝙧𝙤𝙣. #]\n"
         response += "\n".join(user_ids)
         await message.reply_text(response)
    else:
        await message.reply_text(f"حهذا الامر ليس لك ✨")



@app.on_message(filters.command(["مسح المكتومين"], ""), group=136)
async def unmute_all(client, message):
   usr = await client.get_chat(message.from_user.id)
   name = usr.first_name
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7728230165:
    global muted_users
    count = len(muted_users)
    chat_id = message.chat.id
    failed_count = 0

    for member in muted_users.copy():
        user_id = member
        try:
            muted_users.remove(member)
        except Exception:
            failed_count += 1

    successful_count = count - failed_count

    if successful_count > 0:
        await message.reply_text(f"تم الغاء كتم عن {successful_count} من المكتومين ✨")
    else:
        await message.reply_text("لا يوجد مستخدمين مكتومين علشان امسحهم ✨")

    if failed_count > 0:
        await message.reply_text(f"اسف ✨ \nفشل في الغاء الكتم عن {failed_count} من المكتومين ✨")
   else:
        await message.reply_text(f"هذا الامر ليس لك ✨")                                  