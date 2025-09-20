from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus, ChatMembersFilter, ChatType
from pyrogram.types import ChatPrivileges, Message
from config import OWNER_ID
import asyncio
import re
from pyrogram import Client, filters
from datetime import datetime
from pyrogram import enums
from config import OWNER_ID
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from VeRoNMusic import app
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import *
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.enums import ChatMembersFilter
import asyncio
import requests
from VeRoNMusic import app
from VeRoNMusic.core.call import KIM
from VeRoNMusic.utils.decorators import AdminRightsCheck
from datetime import datetime
from config import BANNED_USERS, MONGO_DB_URI, OWNER_ID
from VeRoNMusic.utils import bot_sys_stats
from VeRoNMusic.utils.decorators.language import language
import random
import time
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
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
from pyrogram.errors import PeerIdInvalid
from os import getenv
from VeRoNMusic.misc import SUDOERS
from pyrogram import filters, Client
from telegraph import upload_file
from dotenv import load_dotenv
from VeRoNMusic.utils.database import (set_cmode,get_assistant) 
from VeRoNMusic.utils.decorators.admins import AdminActual
from VeRoNMusic import app
from pyromod import listen

@app.on_message(filters.command(["رفع ادمن"], prefixes="") & filters.group, group=488384838)
async def promote_admin(client: Client, message: Message):
    try:
        # التحقق من صلاحيات المرسل
        promoter = await client.get_chat_member(message.chat.id, message.from_user.id)
        if promoter.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply("❌ هذا الأمر للمشرفين والمالكين فقط!")

        # التحقق من صلاحيات البوت
        bot_member = await client.get_chat_member(message.chat.id, (await client.get_me()).id)
        if not bot_member.privileges.can_promote_members:
            return await message.reply("⚠️ ليس لدي صلاحية تعيين مشرفين!")

        # الحصول على المستخدم المستهدف
        if message.reply_to_message:
            target_user = message.reply_to_message.from_user
        elif len(message.command) > 1:
            target_user = await client.get_users(message.command[1])
        else:
            return await message.reply("↢ يرجى الرد على المستخدم أو كتابة المعرف")

        # تعيين الصلاحيات
        privileges = ChatPrivileges(
            can_change_info=False,
            can_delete_messages=True,
            can_restrict_members=False,
            can_invite_users=True,
            can_manage_video_chats=True,
            can_pin_messages=True,
            can_promote_members=False,
            can_manage_chat=True
        )

        # تنفيذ الترقية بدون معلمة title
        await client.promote_chat_member(
            chat_id=message.chat.id,
            user_id=target_user.id,
            privileges=privileges
        )

        # إعداد رسالة الصلاحيات
        active_permissions = [
            ("🗑️", "حذف الرسائل", privileges.can_delete_messages),
            ("⛔", "حظر المستخدمين", privileges.can_restrict_members),
            ("📨", "إدارة الدعوات", privileges.can_invite_users),
            ("📌", "تثبيت الرسائل", privileges.can_pin_messages),
            ("🎥", "إدارة البثوث", privileges.can_manage_video_chats),
            ("⚙️", "إدارة المجموعة", privileges.can_manage_chat)
        ]

        promotion_msg = "✅ تم الترقية بنجاح!\n\n"
        promotion_msg += f"👤 المستخدم: {target_user.mention}\n\n"
        promotion_msg += "🔹 الصلاحيات الممنوحة:\n"
        promotion_msg += "\n".join(
            f"{icon} {permission}"
            for icon, permission, enabled in active_permissions
            if enabled
        )

        await message.reply(promotion_msg)

    except Exception as e:
        await message.reply(f"❌ حدث خطأ: {str(e)}")
@app.on_message(filters.command(["تنزيل ادمن"], prefixes="") & filters.group, group=84838584848)
async def demote_admin(client: Client, message: Message):
    # التحقق من صلاحيات المرسل
    try:
        demoter = await client.get_chat_member(message.chat.id, message.from_user.id)
        if demoter.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply("❌ هذا الأمر للمشرفين والمالكين فقط!")
    except Exception as e:
        return await message.reply(f"حدث خطأ: {e}")

    # الحصول على المستخدم المستهدف
    try:
        if message.reply_to_message:
            target_user = message.reply_to_message.from_user
        elif len(message.command) > 1:
            target_user = await client.get_users(message.command[1])
        else:
            return await message.reply("↢ يرجى الرد على المستخدم أو كتابة المعرف")
    except Exception as e:
        return await message.reply(f"حدث خطأ: {e}")

    try:
        await client.promote_chat_member(
            chat_id=message.chat.id,
            user_id=target_user.id,
            privileges=ChatPrivileges()  # إزالة جميع الصلاحيات
        )
        await message.reply(f"✅ تم تنزيل {target_user.mention} من الإشراف بنجاح!")
    except Exception as e:
        await message.reply(f"❌ فشل في التنزيل: {str(e)}")


@app.on_message(filters.command(["رتبتي"], prefixes="") & filters.group, group=4838483848)
async def show_rank(client: Client, message: Message):
    try:
        member = await client.get_chat_member(message.chat.id, message.from_user.id)
        
        rank_text = "📊 رتبتك الحالية:\n"
        
        if member.status == ChatMemberStatus.OWNER:
            rank_text += "👑 مالك المجموعة"
        elif member.status == ChatMemberStatus.ADMINISTRATOR:
            rank_text += "🛡 مشرف المجموعة"
            if member.custom_title:
                rank_text += f"\n📛 اللقب: {member.custom_title}"
            if member.privileges:
                rank_text += "\n\nالصلاحيات:\n"
                if member.privileges.can_change_info: rank_text += "- تغيير معلومات المجموعة\n"
                if member.privileges.can_delete_messages: rank_text += "- حذف الرسائل\n"
                if member.privileges.can_restrict_members: rank_text += "- حظر المستخدمين\n"
                if member.privileges.can_invite_users: rank_text += "- إدارة الدعوات\n"
                if member.privileges.can_manage_video_chats: rank_text += "- إدارة البثوث\n"
        elif message.from_user.id == OWNER_ID:
            rank_text += "🔥 مطور البوت الرئيسي"
        else:
            rank_text += "👤 عضو عادي"
        
        await message.reply(rank_text)
    except Exception as e:
        await message.reply(f"حدث خطأ: {e}")


@app.on_message(filters.command(["الادمنيه"], prefixes="") & filters.group, group=63636)
async def list_admins(client: Client, message: Message):
    try:
        admins = []
        async for m in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
            if m.user.is_bot: continue
            
            admin_info = f"- {m.user.mention}"
            if m.custom_title:
                admin_info += f" 📛 {m.custom_title}"
            
            admins.append(admin_info)
        
        await message.reply(f"👥 قائمة المشرفين:\n{chr(10).join(admins)}")
    except Exception as e:
        await message.reply(f"حدث خطأ: {e}")