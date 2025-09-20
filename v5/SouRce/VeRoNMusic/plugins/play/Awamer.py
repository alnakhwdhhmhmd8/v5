import asyncio
import config
import re
import os
import requests
from os import getenv
from pyrogram import Client, filters
from VeRoNMusic import app
from config import OWNER_ID
from pyrogram import filters, Client
from pyrogram import filters
from pyrogram import Client
from typing import Union
from aiohttp import ClientSession
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.enums import ChatMemberStatus, ParseMode
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from VeRoNMusic.misc import SUDOERS
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from VeRoNMusic.utils.database import (set_cmode,get_assistant)
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
from datetime import datetime
from pyrogram import enums
from config import OWNER_ID
from pyrogram.errors import MessageNotModified


from pyrogram.types import CallbackQuery

from pyrogram.types import CallbackQuery, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from VeRoNMusic import app
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import *
from pyrogram.enums import ChatMembersFilter
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup                           
import asyncio
from VeRoNMusic import (Apple, Resso, SoundCloud, Spotify, Telegram)
from VeRoNMusic import app
import pyrogram
from VeRoNMusic.misc import SUDOERS
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from config import OWNER_ID
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from pyrogram.enums import ParseMode
from VeRoNMusic import app
from VeRoNMusic.utils.database import is_on_off




amaerrof = []

@app.on_message(filters.command(["قفل الاوامر", "تعطيل الاوامر"], ""), group=277288870000127181882)
async def amaerrlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 6753126490:
      if message.chat.id in amaerrof:
        return await message.reply_text("الاوامر معطله من قبل\n༄")
      amaerrof.append(message.chat.id)
      return await message.reply_text("تم تعطيل الاوامر بنجاح\n༄")
   else:
      return await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس\n༄")

@app.on_message(filters.command(["فتح الاوامر", "تفعيل الاوامر"], ""), group=726262766000288)
async def amaerropen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 6753126490:
      if not message.chat.id in amaerrof:
        return await message.reply_text("الاوامر مفعله من قبل\n")
      amaerrof.remove(message.chat.id)
      return await message.reply_text("تم تفعيل الاوامر بنجاح\n༄")
   else:
      return await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس\n༄")




user = ""

@app.on_message(filters.command(["اوامر", "الاوامر"], ""), group=726272728281)
async def mmmy(client: Client, message: Message):
    global user
    user = message.from_user.id
    if message.chat.id in amaerrof:
        return await message.reply_text("الاوامر معطله من قبل الادمن\n༄")
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 6753126490:
        await message.reply_video(
            video="https://files.catbox.moe/uv47pv.jpg",
            caption=f"[سوࢪس 𝐉𝐀𝐊- | 𝙎𝙤𝙪𝙧𝙘𝙚 𝐉𝐀𝐊-. #]\n[ ♕ قائمــة الاوامــر  ♕ ] \n✦┅━╍━╍╍━━╍━━╍━┅✦\n- مرحبا بك عزيز المستخدم هذه هي قائمة اوامر السورس \n\n❬ 1 ❭ اوامر حماية المجموعه ⚙️\n❬ 2 ❭ اوامر اصحاب الرتب 👮‍♂️\n❬ 3 ❭ اوامر الاعضاء 💫\n❬ 4 ❭ اوامر المطورين \n❬ 5 ❭ اوامر الموسيقي 🎵\n❬ 6 ❭ اوامر التسليه 🥳",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "꙳. ❶.꙳", callback_data="lockdd"
                        ),
                        InlineKeyboardButton(
                            "꙳.❷.꙳", callback_data="abimnn"
                        ),

                        InlineKeyboardButton(
                            "꙳.❸.꙳", callback_data="Maalek"
                        ),
                    ],
                    [
                        InlineKeyboardButton("꙳.❹.꙳", callback_data="deeev"),
                        InlineKeyboardButton("꙳.❺.꙳", callback_data="playyy"),
                    ],
                    [
                        InlineKeyboardButton("꙳.❻.꙳", callback_data="gamess"),
                    ],
                    [
                        InlineKeyboardButton("ᴠᴇʀᴏɴ", url=SUPPORT_CHANNEL),
                    ],
                ]
            )
        )
    else:
        await message.reply("هذا الامر يخص ❪ الادمن وفوق ❫ بس\n༄")


# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂[VERON]▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂



@app.on_callback_query(filters.regex("Musicveron"), group=1863738666666655582)
async def mpdtsf(client, query: CallbackQuery):
    global user
    chat = query.message.chat
    get = await client.get_chat_member(chat.id, query.from_user.id)
    user_status = get.status
    if query.from_user.id != user:
        await client.answer_callback_query(query.id, text="هييه مايمديك الامر ياروعه!!", show_alert=True)
        return

    await client.answer_callback_query(query.id)
        
    await query.answer("Musicveron")
    await query.edit_message_text(
        f"""[سوࢪس 𝐉𝐀𝐊- | 𝙎𝙤𝙪𝙧𝙘𝙚 𝐉𝐀𝐊-. #]\n[ ♕ قائمــة الاوامــر  ♕ ] \n✦┅━╍━╍╍━━╍━━╍━┅✦\n- مرحبا بك عزيز المستخدم هذه هي قائمة اوامر السورس \n\n❬ 1 ❭ اوامر حماية المجموعه ⚙️\n❬ 2 ❭ اوامر اصحاب الرتب 👮‍♂️\n❬ 3 ❭ اوامر الاعضاء 💫\n❬ 4 ❭ اوامر المطورين \n❬ 5 ❭ اوامر الموسيقي 🎵\n❬ 6 ❭ اوامر التسليه 🥳""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                    "꙳.❶.꙳", callback_data="lockdd"),       
                    InlineKeyboardButton(
                    "꙳.❷.꙳", callback_data="abimnn"),
                    InlineKeyboardButton(
                    "꙳.❸.꙳", callback_data="Maalek"),
                ],[
                    InlineKeyboardButton("꙳.❹.꙳", callback_data="deeev"),
                   InlineKeyboardButton("꙳.❺.꙳", callback_data="playyy"),
                ],[
                   InlineKeyboardButton("꙳.❻.꙳", callback_data="gamess"),   
                ],[        
                    InlineKeyboardButton("ᴠᴇʀᴏɴ", url=SUPPORT_CHANNEL),
                ],
            ]
        )
    )

# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂[الحمايه 1]▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂


@app.on_callback_query(filters.regex("lockdd"), group=14)
async def playyy(client, query: CallbackQuery):
    global user
    chat = query.message.chat
    get = await client.get_chat_member(chat.id, query.from_user.id)
    user_status = get.status
    if query.from_user.id != user:
        await client.answer_callback_query(query.id, text="هييه مايمديك الامر ياروعه!!", show_alert=True)
        return

    await client.answer_callback_query(query.id)
    
    await query.answer ("lockdd")
    await query.edit_message_text(
        f"""
[سوࢪس 𝐉𝐀𝐊- | 𝙎𝙤𝙪𝙧𝙘𝙚 𝐉𝐀𝐊-. #]
[ ♕ قائمــة اوامر حماية المجموعه  ♕ ] 
✦┅━╍━╍╍━━╍━━╍━┅✦
- مرحبا بك عزيز المستخدم هذه هي قائمة اوامر السورس 
✦┅━╍━╍╍━━╍━━╍━┅✦
🔐 ╖ قفل «» فتح + الامر 
⁦♻️⁩ ╜ قفل «» فتح ❬ الكـــل ❭ 
✦┅━╍━╍╍━━╍━━╍━┅✦
📮╖ الدردشه
📜╢ المعرفات
📸╢ الصور
📽️╢ الفيديوهات
🎟╢ الاستيكر
📂╢ الملفات
🎥╢ المتحركه
⏏️╢ الرفع
🔊╢ الريكورد
🎧╢ الصوت
📞╢ الجهات
🔊╢ الترحيب
🚫╢ المغادره
🎧╢ الاغاني
🏨╢ الزخرفه
🍿╢ الافلام
🎬╢ اليوتيوب
💱╢ الترجمه
🔄╢ الردود
🚿╢ التوجيه
🗳️╢ الاشعارات
💳╢ التاج
🧾╢ رابط الحذف
🆔╢ الايدي بالصوره
🔈╢ اطردني
🤔╢ مين ضافني
🏓╢ الالعاب
🎁╢ الروايات
🎆╢ الابراج
🔍╢ معاني الاسماء
💬╢ الترحيب
🌐╢ الروابط
🔄╢ التوجيه
🍿╢ الفشار
⚜️╢ البوتات
⚠️╜ الممنوعه
✦┅━╍━╍╍━━╍━━╍━┅✦
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="Musicveron")]]
        ),
    )





# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂[الادمن 2]▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂



@app.on_callback_query(filters.regex("abimnn"), group=120517665581)
async def lockdd(client, query: CallbackQuery):
    global user
    chat = query.message.chat
    get = await client.get_chat_member(chat.id, query.from_user.id)
    user_status = get.status
    if query.from_user.id != user:
        await client.answer_callback_query(query.id, text="هييه مايمديك الامر ياروعه!!", show_alert=True)
        return

    await client.answer_callback_query(query.id)
    
    await query.answer ("abimnn")
    await query.edit_message_text(
        f"""
[سوࢪس 𝐉𝐀𝐊- | 𝙎𝙤𝙪𝙧𝙘𝙚 𝐉𝐀𝐊-. #]
[ ♕ قائمــة اوامر اصحاب الرتب  ♕ ] 
✦┅━╍━╍╍━━╍━━╍━┅✦
- مرحبا بك عزيز المستخدم هذه هي قائمة اوامر السورس 
✦┅━╍━╍╍━━╍━━╍━┅✦
🐣 « الادمن » ⇊
✦┅━╍━╍╍━━╍━━╍━┅✦
🥳╖ رفع مميز «» تنزيل مميز
🙋╢ الترحيب
🤬╢ اضف مغادره «» مسح المغادره
💩╢ رساله المغادره
🤖╢ كشف البوتات
🥳╢ المميزين «» حذف المميزين
🛡╢ حظر «» الغاء حظر
🗡╢ كتم «» الغاء كتم
🗑╢ حظر لمده + المده
🧺╢ كتم لمده + المده
😠╢ طرد «» تطهير 
📌╢ تثبيت «» تثبيت بدون اشعار
🧷╜ الغاء تثبيت الكل
✦┅━╍━╍╍━━╍━━╍━┅✦
🤵 « المنشئ » ⇊
✦┅━╍━╍╍━━╍━━╍━┅✦
🐣╖ رفع «» تنزيل ادمن
💌╢ اضف «» حذف  ❬ رد ❭
👨‍🎨╢ الردود «» حذف الردود
🔕╢ ايقاف المنشن
💫╢ تعيين «» مسح  ❬ الايدي ❭
🍫╢ الادمنيه «» حذف الادمنيه
🍻╢ اضف ترحيب
🎲╢ حذف المحظورين «» المكتومين
🎯╢ منع + الكلمه
🚜╢ الغاء منع + الكلمه
🚨╢ حذف الكلمات الممنوعه
🔍╢ المميزين عام
📚╜ ❬ + ❭ جميع ماسبق
✦┅━╍━╍╍━━╍━━╍━┅✦
👮‍♂️ « المالك » ⇊
✦┅━╍━╍╍━━╍━━╍━┅✦
🔼╖ اضف صوره «» وصف (للجروب)
🤵╢ رفع منشئ «» تنزيل منشئ
🔊╢ تاج للاعضاء «» للكل
🔗╢ اضف رابط «» مسح الرابط
🔏╢ اضف اسم «» تحديث
🍿╢ المنشئين «» حذف المنشئين
📚╜ ❬ + ❭ جميع ماسبق
✦┅━╍━╍╍━━╍━━╍━┅✦
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="Musicveron")]]
        ),
    )





# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂[اوامر الاعضاء 3]▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂



@app.on_callback_query(filters.regex("Maalek"), group=119340009986)
async def abinmnn(client, query: CallbackQuery):
    global user
    chat = query.message.chat
    get = await client.get_chat_member(chat.id, query.from_user.id)
    user_status = get.status
    if query.from_user.id != user:
        await client.answer_callback_query(query.id, text="هييه مايمديك الامر ياروعه!!", show_alert=True)
        return

    await client.answer_callback_query(query.id)
    
    await query.answer ("Maalek")
    await query.edit_message_text(
        f"""
[سوࢪس 𝐉𝐀𝐊- | 𝙎𝙤𝙪𝙧𝙘𝙚 𝐉𝐀𝐊-. #]
[ ♕ قائمــة اوامر الاعضاء  ♕ ] 
✦┅━╍━╍╍━━╍━━╍━┅✦
- مرحبا بك عزيز المستخدم هذه هي قائمة اوامر السورس 
✦┅━╍━╍╍━━╍━━╍━┅✦
🎤╖ غنيلي «» حساب العمر
🖼️╢ صورتي «» نسبه جمالي
📸╢ استوري «» رمزيات
📖╢ قرءان
⚙️╢ الاعدادات
🔘╢ نقاطي
⚜️╢ حذف «» بيع ❬ نقاطي ❭
💌╢ رسائلي «» حذف ❬ رسائلي ❭
🔊╢ زخرفه «» اغاني 
🎥╢ افلام «» كارتون
🧭╢ ترجمه + روايات
📼╢ يوتيوب «» العاب
🌡╢ طقس + المنطقة 
🦞╢ ثيو «» الرابط
🥱╢ اسمي «» الرتبه
💞╢ بحبك «» تتجوزيني
⚕️╢ جهاتي «» حذف جهاتي
☣️╢ صلاحياتي «» بينج
🔉╢ قول + الكلمه
⛔️╢ الكلمات الممنوعه
⭐️╢ انا مين «» انا فين
♻️╢ قول + الكلمه
🐕╢ قطه «» كلب 
💔╢ اطردني «» اكتمني
🌐╢ تاك للاونلاين «» تاك للاعضاء
👨‍🏫╢ سورس «» المطور
♋️╢ الرابط «» ايدي
⬆️╢ رتبتي «» كشف
📊╢ رد  انت يا بوت
🤔╢ اي رايك يابوت
😈╢ هينو «» هينها
💋╢ بوسو «» بوسها
🙊╢ بتحب دي «» بتحب ده
⚠️╜ رابط الحذف
✦┅━╍━╍╍━━╍━━╍━┅✦
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="Musicveron")]]
        ),
    )





# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂[المطورين 4]▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂


@app.on_callback_query(filters.regex("deeev"), group=119366065445687746)
async def Maalek(client, query: CallbackQuery):
    global user
    chat = query.message.chat
    get = await client.get_chat_member(chat.id, query.from_user.id)
    user_status = get.status
    if query.from_user.id != user:
        await client.answer_callback_query(query.id, text="هييه مايمديك الامر ياروعه!!", show_alert=True)
        return

    await client.answer_callback_query(query.id)
    
    await query.answer ("deeev")
    await query.edit_message_text(
        f"""
[سوࢪس 𝐉𝐀𝐊- | 𝙎𝙤𝙪𝙧𝙘𝙚 𝐉𝐀𝐊-. #]
[ ♕ قائمــة اوامر المطورين  ♕ ] 
✦┅━╍━╍╍━━╍━━╍━┅✦
- مرحبا بك عزيز المستخدم هذه هي قائمة اوامر السورس 
✦┅━╍━╍╍━━╍━━╍━┅✦
👮‍♂️ « المطور » ⇊
✦┅━╍━╍╍━━╍━━╍━┅✦
🤴╖ رفع «» تنزيل ❬ مالك ❭
🔂╢ تغيير رابط الجروب
🔊╢ اذاعه بالمجموعات
👨‍🏭╢ اذاعه بالتوجيه للمجموعات
🤹‍♀╢ اذاعه موجهه بالتثبيت
☀️╢ اذاعه خاص
💘╢ اذاعه بالتوجيه خاص
🎙️╢ اذاعه بالتثبيت
📶╢ جلب نسخه احتياطيه
🏋‍♂╢ رفع نسخه احتياطيه
🍃╢ الاحصائيات
🚷╢ حذف المالكين
📚╜ ❬ + ❭ جميع ماسبق
✦┅━╍━╍╍━━╍━━╍━┅✦
💎 « المطور الاساسي » ⇊
✦┅━╍━╍╍━━╍━━╍━┅✦
📑╖ اضف «» حذف رد عام
🤴╢ رفع «» تنزيل ❬ مميز عام ❭
💎╢ مسح المميزين عام
🗃️╢ الردود العامه
🧨╢ حذف الردود العامه
🛠╢ اذاعه بالتوجيه خاص
🍃╢ اذاعه بالتوجيه للمجموعات
🎯╢ اذاعه بالتثبيت
☀️╢ اذاعه موجهه بالتثبيت
🧲╢ جلب «» رفع ❬نسخه احتياطيه❭
⏳╢ الاحصائيات
🤴╢ رفع «» تنزيل ❬ مطور ❭
🤖╢ المطورين «» حذف المطورين
🔗╢ ضع اسم للبوت
📝╢ تغيير رساله المغادره
🚫╢ حظر «» كتم  ❬ عام ❭
🥺╢ المكتومين  عام 
💔╢ المحظورين عام
♻️╢ الغاء العام
📚╜ ❬ + ❭ جميع ماسبق
✦┅━╍━╍╍━━╍━━╍━┅✦
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="Musicveron")]]
        ),
    )
    

# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂[الموسيقي 5 ]▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂


@app.on_callback_query(filters.regex("playyy"), group=1445687746)
async def gamess(client, query: CallbackQuery):
    global user
    chat = query.message.chat
    get = await client.get_chat_member(chat.id, query.from_user.id)
    user_status = get.status
    if query.from_user.id != user:
        await client.answer_callback_query(query.id, text="هييه مايمديك الامر ياروعه!!", show_alert=True)
        return

    await client.answer_callback_query(query.id)
    
    await query.answer ("playyy")
    await query.edit_message_text(
        f"""
[سوࢪس 𝐉𝐀𝐊- | 𝙎𝙤𝙪𝙧𝙘𝙚 𝐉𝐀𝐊-. #]
[ ♕ قائمــة اوامر الموسيقي للقنوات والجروبات  ♕ ] 
✦┅━╍━╍╍━━╍━━╍━┅✦
- مرحبا بك عزيز المستخدم هذه هي قائمة اوامر السورس 
✦┅━╍━╍╍━━╍━━╍━┅✦
▶️╖ تشغيل «» ريبلاي علي اغنيه
🎶╢ تشغيل + اسم الاغنيه
📹╢ فيديو + اسم الفديو
🔴╢ تشغيل + لينك بث مباشر
⏹╢ ايقاف
⏯️╢ تخطي
👷‍♂️╜ الحساب المساعد
✦┅━╍━╍╍━━╍━━╍━┅✦
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="Musicveron")]]
        ),
    )

# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂[التسليه 6 ]▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂


@app.on_callback_query(filters.regex("gamess"), group=777)
async def deeeeev(client, query: CallbackQuery):
    global user
    chat = query.message.chat
    get = await client.get_chat_member(chat.id, query.from_user.id)
    user_status = get.status
    if query.from_user.id != user:
        await client.answer_callback_query(query.id, text="هييه مايمديك الامر ياروعه!!", show_alert=True)
        return

    await client.answer_callback_query(query.id)
    
    await query.answer("gamess")
    await query.edit_message_text(
        f"""
[سوࢪس 𝐉𝐀𝐊- | 𝙎𝙤𝙪𝙧𝙘𝙚 𝐉𝐀𝐊-. #]
[ ♕ قائمــة اوامر التسليه  ♕ ] 
✦┅━╍━╍╍━━╍━━╍━┅✦
- مرحبا بك عزيز المستخدم هذه هي قائمة اوامر السورس 
✦┅━╍━╍╍━━╍━━╍━┅✦
╖ لوخيروك
╢ كت + تويت
╢ لعبة ورقه حجره 
╢ نمله
╢ صرصار
╢ خنزير
╢ رقص
╢ ابراج
╢ قتل
╢ تف
╢ مح
╢ صور
╢ اعلام
╢ معاني
╢ نداء
╢ زوجني + ز
╢ الساعه
╢ مشاهير
╢ ممثلين 
╢ لاعبين
╢ صور بنات
╢ صور شباب 
╢ صور انميي
╢ قرآن
╢ مهنتي
╢ حظ
╢ سله
╢ كوره
╢ سهم
╢ اقتباس
╢ متحركه
╢ انصحني
╢ اصراحه
╢ حكمه
╜ اذكار
✦┅━╍━╍╍━━╍━━╍━┅✦
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="Musicveron")]]
        ),
    )