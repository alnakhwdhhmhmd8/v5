import asyncio
import re
import time
import requests
import aiohttp
from pyrogram import Client, filters
from datetime import datetime
from pyrogram import enums
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import CallbackQuery, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.enums import ChatMemberStatus, ParseMode
from VeRoNMusic import app
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import *
from pyrogram.enums import ChatMembersFilter
from telegraph import upload_file
from asyncio import gather
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import *
from pyrogram.enums import ChatMembersFilter
import asyncio

from pyrogram.enums import ParseMode

from VeRoNMusic import app





def is_owner(_, __, message):

    return message.from_user.id == OWNER_ID


chat_locked = False
mention_locked = False
video_locked = False
link_locked = False
sticker_locked = False
forward_locked = False
photo_locked = False
saap_locked = False


@app.on_message(filters.command(["قفل الدردشه","قفل الدردشة"], ""), group=721136)
async def enabled(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        await app.set_chat_permissions(message.chat.id,  ChatPermissions(can_send_messages=False))
        await message.reply_text(f"تم قفل الدرشه {message.from_user.mention}بنجاح ✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")        
  
                       
@app.on_message(filters.command(["فتح الدردشه","فتح الدردشة"], ""), group=65421136)
async def undard(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        await app.set_chat_permissions(message.chat.id, ChatPermissions(can_send_messages=True))
        await message.reply_text(f"تم فتح الدرشه {message.from_user.mention}بنجاح ✨")        
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
    
    
@app.on_message(filters.command("قفل التثبيت", ""), group=8666786)
async def taspit(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        await app.set_chat_permissions(message.chat.id, ChatPermissions(
        can_pin_messages=False,
        can_send_messages=True))
        await message.reply_text(f"تم  التثبيت {message.from_user.mention}بنجاح ✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
      
   
@app.on_message(filters.command("فتح التثبيت", ""), group=8836)
async def tasspit(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        await app.set_chat_permissions(message.chat.id, ChatPermissions(
        can_pin_messages=True,
        can_send_messages=True))
        await message.reply_text(f"ابشر {message.from_user.mention}\n لقد فتحت التثبيت✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
    
 
@app.on_message(filters.command("قفل الدعوة", ""), group=7890986)
async def dasoo(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        await app.set_chat_permissions(message.chat.id, ChatPermissions(
        can_invite_users=False,
        can_send_messages=True))
        await message.reply_text(f"تم قفل الدعوه {message.from_user.mention} بنجاح ✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
       
   
@app.on_message(filters.command("فتح الدعوة", ""), group=8881636)
async def zombeee(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        await app.set_chat_permissions(message.chat.id, ChatPermissions(
        can_invite_users=True,
        can_send_messages=True))
        await message.reply_text(f"تم فتح الدعوه {message.from_user.mention} بنجاح ✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
       
   
@app.on_message(filters.command("قفل الميديا", ""), group=6788600)
async def mediazomb(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        await app.set_chat_permissions(message.chat.id, ChatPermissions(
        can_invite_users=True,
        can_send_media_messages=False,
        can_send_messages=True))
        await message.reply_text(f"ابشر {message.from_user.mention}\nلقد قفلت الميديا✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
       
   
@app.on_message(filters.command("فتح الميديا", ""), group=87736)
async def zombmeddia(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        await app.set_chat_permissions(message.chat.id, ChatPermissions(
        can_send_media_messages=True,
        can_send_messages=True))
        await message.reply_text(f"ابشر {message.from_user.mention}\nلقد فتحت الميديا✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
       
   
@app.on_message(filters.command("قفل المتحركات", ""), group=6136)
async def motahark(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        await app.set_chat_permissions(message.chat.id, ChatPermissions(
        can_invite_users=True,
        can_send_media_messages=True,
        can_send_other_messages=False,
        can_send_messages=True))
        await message.reply_text(f"ابشر {message.from_user.mention}\nلقد قفلت المتحركات✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
     
  
@app.on_message(filters.command("فتح المتحركات", ""), group=31136)
async def motazombie(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        await app.set_chat_permissions(message.chat.id, ChatPermissions(
        can_send_other_messages=True,
        can_send_messages=True))
        await message.reply_text(f"ابشر {message.from_user.mention}\nلقد فتحت المتحركات✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
     
  
@app.on_message(filters.regex("قفل المنشن"), group=829636)
async def lock_mention(client, message):
    global mention_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        mention_locked = True
        await message.reply_text(f"ابشر {message.from_user.mention}\nلقد قفلت المنشن✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
    


@app.on_message(filters.regex("فتح المنشن"), group=16536)
async def unlock_mention(client, message):
    global mention_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        mention_locked = False
        await message.reply_text(f"ابشر {message.from_user.mention}\nلقد فتحت المنشن✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
    
    


@app.on_message(filters.regex("قفل الفيديو"), group=90656)
async def lock_video(client, message):
    global video_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        video_locked = True
        await message.reply_text(f"ابشر {message.from_user.mention}\nلقد قفلت الفيديو✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
    

@app.on_message(filters.regex("فتح الفيديو"), group=827876)
async def unlock_video(client, message):
    global video_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        video_locked = False
        await message.reply_text(f"ابشر {message.from_user.mention}\nلقد فتحت الفيديو✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
    



@app.on_message(filters.regex("قفل التوجيه"), group=2536)
async def lock_forward(client, message):
    global forward_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:    
        forward_locked = True
        await message.reply_text(f"ابشر {message.from_user.mention}\nلقد قفلت التوجيه✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
    

@app.on_message(filters.regex("فتح التوجيه"), group=70096)
async def unlock_forward(client, message):
    global forward_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        forward_locked = False
        await message.reply_text(f"ابشر {message.from_user.mention}\nلقد فتحت التوجيه✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
    



@app.on_message(filters.regex("قفل الملصقات"), group=81056)
async def lock_stickers(client, message):
    global sticker_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        sticker_locked = True
        await message.reply_text(f"ابشر {message.from_user.mention}\nلقد قفلت الملصقات✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
    

@app.on_message(filters.regex("فتح الملصقات"), group=7636)
async def unlock_stickers(client, message):
    global sticker_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        sticker_locked = False
        await message.reply_text(f"ابشر {message.from_user.mention}\nلقد فتحت الملصقات✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
    





@app.on_message(filters.regex("قفل الصور"), group=820036)
async def lock_photos(client, message):
    global photo_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        photo_locked = True
        await message.reply_text(f"ابشر {message.from_user.mention}\nلقد قفلت الصور✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
    

@app.on_message(filters.regex("فتح الصور"), group=826006)
async def unlock_photos(client, message):
    global photo_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        photo_locked = False
        await message.reply_text(f"ابشر {message.from_user.mention}\nلقد فتحت الصور✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
    



@app.on_message(filters.regex("قفل الروابط"), group=865136)
async def lock_link(client, message):
    global link_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        link_locked = True
        await message.reply_text(f"ابشر {message.from_user.mention}\nلقد قفلت الروابط✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
    

@app.on_message(filters.regex("فتح الروابط"), group=826341516)
async def unlock_link(client, message):
    global link_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        link_locked = False
        await message.reply_text(f"ابشر {message.from_user.mention}\nلقد فتحت الروابط✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
      




@app.on_message(filters.regex("قفل السب"), group=82637277647376)
async def lock_saapa(client, message): 
    global saap_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        saap_locked = True
        await message.reply_text(f"ابشر {message.from_user.mention}\nلقد قفلت السب ✨")
        await delete_message(client, message)
    else:
        await message.reply_text("هذا الامر ليس لك ✨")


@app.on_message(filters.regex("فتح السب"), group=826372647436)
async def unlock_saap(client, message):
    global saap_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        saap_locked = False
        await message.reply_text(f"ابشر {message.from_user.mention}\nلقد فتحت السب✨")
        await delete_message(client, message)
    else:
        await message.reply_text("هذا الامر ليس لك ✨")


@app.on_message(filters.text & ~filters.create(is_owner) & filters.create(lambda _, __, message: saap_locked), group=56)
async def delete_sapa(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.MEMBER]:
        if "احا" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨") 
        elif "خخخ" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨") 
        elif "كسك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨") 
        elif "كسمك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨") 
        elif "عرص" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨") 
        elif "خول" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨") 
        elif "يبن" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨") 
        elif "كلب" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب .✨") 
        elif "علق" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n • ممنوع السب✨")
        elif "كسم" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "سسس" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "كسمكم" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يابن متناكه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يمتناكه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يمتناك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "عرص" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "عرث" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "خول" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "الخول" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "سكس" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "كسي" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "كسم فيرون" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "طيز" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "متيظز" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "طيزو" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "طيزي" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "تيز" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "تيزك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "كسس" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "نيك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "هنيكك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "نيكو" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "نكت" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "ناكك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "معيرص" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "كسماك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "كوسك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يبن القحبه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "القحبه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "مك متناكه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "امك صحبتي" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يابن الفاجره" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "الفاجره" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "شرموطه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "شرمود" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "شرموط" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "صايع" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "كلب" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "كلبي" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "بت متناكه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "بت المتناكه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "العاهره" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "كسمكم" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "بت فجره" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "بت الفجره" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يولاد متناكه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "كسم اللي فجروب" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "كسمكم" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يولاد القحابي" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "هلف" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "حلوف" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "مجلخ" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "حمار" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "تيث" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "تيوس" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "تيس" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "جبان" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "شخ" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "خخخخ" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "خهخهخهههه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "خخخخخخخه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "طري" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "زبي" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "تع مصمص" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "تعالي مص" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "مصمصلي فيزبي" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "زبي" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "دخلو" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "ادخلو" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "انتشك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "زاني" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يا ابن الزنيه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يا بت الزنيه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يبن زانيه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يبن زنيه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يبت زانيه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "العبي فكسك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "ظيزك كبيره" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "بزازك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "بز" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "كسو" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "كسمو" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "كسمه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "كساس" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "عره" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "كس مجلخ" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "كلابي" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "كسم كيمي" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "بضاني" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "تع لحوص" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "هنيكك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "هفشخك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "هفشخو" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "فشختو" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "هنيك امك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "نكت امك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "امك الشرموطه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "امك متنكه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "امك متناكه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "طيزها" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "معتوه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "كس" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "زب" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يا ابن متناك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يابن المتناكه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يفاجر" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يا فجره" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يفجره" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "هياج" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "هيجه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يبن الهيجه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يابن الهيجه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يبت الهيجه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يا هيجه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يا بت الهيجه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يا خروف" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "ابن المتناكه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "متناك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "انكك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "ياهطل" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "متنكهه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "علق" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "تسك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "خخخخخخ" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "سكس" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "متناكك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "زبك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "مبعبص" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "خنزير" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "حيوان" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "مره" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يامره" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يبن لمره" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "هنينك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يكس" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "نسوانجي" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "كلبجي" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "خدام" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "بهيم" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "ابن متناكه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "قحبه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "عيل" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "يولاد الوسخه" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")                    
        elif "يولاد قحابي" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")                    
        elif "يولاد المره" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")                   
        elif "منايك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "منيوك" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")                    
        elif "خخخخخخخخ" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "شرمط" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "بلد متناكين" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "بلد" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "خرفان" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "بلد معرصين" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")
        elif "بلد متناكين" in message.text:
            await message.delete()
            await message.reply_text(f"قلبي: {message.from_user.mention}\n ممنوع السب✨")                   
        else:
            pass    


@app.on_message(filters.command("فتح الكل", ""), group=826372774728)
async def vegaa(client, message):
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)	
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        global saap_locked
        global mention_locked
        global link_locked
        global video_locked
        global forward_locked
        global sticker_locked
        global photo_locked
        saap_locked = False
        link_locked = False
        photo_locked = False
        sticker_locked = False
        forward_locked = False
        video_locked = False
        mention_locked = False
        await message.reply_text(f"ابشر {message.from_user.mention}\nلقد فتحت الكل✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
       
   
@app.on_message(filters.command("قفل الكل", ""), group=8263722222112136)
async def VEGAA(client, message):
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:	
        global saap_locked
        global mention_locked
        global link_locked
        global video_locked
        global forward_locked
        global sticker_locked
        global photo_locked
        saap_locked = False
        link_locked = False
        photo_locked = False
        sticker_locked = False
        forward_locked = False
        video_locked = False
        mention_locked = False
        await message.reply_text(f"ابشر {message.from_user.mention}\nلقد قفل الكل✨")
    else:
        await message.reply_text("هذا الامر ليس لك ✨")
       


@app.on_message(filters.command(["الحمايه","اوامر الحمايه"], ""), group=85007761372726)
async def kggalid(client: Client, message: Message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
           await message.reply_photo(
            photo="https://d.uguu.se/yCwrXfeu.jpg",
            caption="""**[سوࢪس فيࢪوטּ | 𝙎𝙤𝙪𝙧𝙘𝙚 𝙑𝙚𝙧𝙤𝙣. #]\n╮❖ياا هلا قلبي اليك\n╯❖اوامر الحمايه من فيࢪون**""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [          
                    InlineKeyboardButton(
                        "« اوامر القفل »", callback_data="xxxtreghjj"),       
                    InlineKeyboardButton(
                        " « اوامر الادمن »", callback_data="hhhuyeikx"),
                ],[
                    InlineKeyboardButton(
                       "ᴠᴇʀᴏɴ", url=f"https://t.me/Source_Veron"),                        
                ],
            ]
        ),
    )
    else:
        await message.reply_text("لازم تكون ع الاقل ادمن او اعلي ✨")




@app.on_message(filters.command(["تفعيل الحمايه","تفعيل الحماية"], ""), group=601123409432)
async def kggalid(client: Client, message: Message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    chat_idd = message.chat.id
    chat_name = message.chat.title
    chat_username = f"@{message.chat.username}"
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
       photo = await client.download_media(message.chat.photo.big_file_id)
       await message.reply_photo(photo=photo, caption=f"""**[سوࢪس فيࢪوטּ | 𝙎𝙤𝙪𝙧𝙘𝙚 𝙑𝙚𝙧𝙤𝙣. #]\n╮❖اهلا قلبي: {message.from_user.mention}\n│᚜❖تم تفعيل الحمايه بنجاح\n│᚜❖في جروب: {chat_name}\n╯❖من سورس فيࢪون**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر الحمايه", callback_data="ssaweed"),
                ],[
                    InlineKeyboardButton("ᴠᴇʀᴏɴ", url="https://t.me/Source_Veron"),
                    ],
            ]
        ),
    )
    else:
        await message.reply_text("لازم تكون ع الاقل ادمن او اعلي ✨")
        



message_counts = {}

@app.on_message(filters.group, group=55727211005)
async def update_message_count(_, message):
    group_id = message.chat.id
    user_id = message.from_user.id
    
    key = (group_id, user_id)
    message_counts.setdefault(key, 0)
    message_counts[key] += 1

async def get_user_name(client, user_id):
    user = await client.get_users(user_id)
    return f"{user.first_name or ''} {user.last_name or ''}"

@app.on_message(filters.command("توب", "") & filters.group, group=55559190191)
async def get_top_users(client, message):
    group_id = message.chat.id   
    top_users = sorted(message_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    response = "<u>افضل عشر توبات لهذا الكروب:</u>\n\n"   
    for rank, ((group_id, user_id), message_count) in enumerate(top_users[:3], start=1):
        user_name = await get_user_name(client, user_id)
        medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉"
        response += f"{medal} {rank} l {user_name} ➥ {message_count} ➥ رسايل\n\n"  
    for rank, ((group_id, user_id), message_count) in enumerate(top_users[3:], start=4):
        user_name = await get_user_name(client, user_id)
        response += f"{rank} l {user_name} ➥ {message_count} ➥ رسايل\n\n"      
    await client.send_message(message.chat.id, response)