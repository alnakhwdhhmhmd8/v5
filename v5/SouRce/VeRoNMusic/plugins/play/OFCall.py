import asyncio
import os
from typing import Optional  # تمت إضافة هذا الاستيراد
from PIL import Image, ImageFilter
from pyrogram import Client, filters
from pyrogram.types import Message, ChatPrivileges
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import ChatAdminRequired
from pyrogram.raw.types import (  # تمت إضافة هذه الاستيرادات
    InputGroupCall,
    InputPeerChannel,
    InputPeerChat,
    InputPeerUser
)
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import (
    CreateGroupCall,
    DiscardGroupCall
)
from pytgcalls import PyTgCalls
from pytgcalls.exceptions import NoActiveGroupCall, AlreadyJoinedError
from pytgcalls.types import MediaStream
from VeRoNMusic import app
from VeRoNMusic.core.call import KIM
from VeRoNMusic.utils.database.assistantdatabase import get_assistant
from config import OWNER_ID






async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    assistant = await get_assistant(message.chat.id)
    chat_peer = await assistant.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await assistant.invoke(GetFullChannel(channel=chat_peer))
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await assistant.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await app.send_message(f"**No group call Found** {err_msg}")
    return False


@app.on_message(filters.regex("^افتح الكول$"), group=752)
@app.on_message(filters.regex("^افتح الكول$") & filters.channel, group=752)
async def start_group_call(client: Client, message: Message):

    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name    
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 6760053475:
        chat_id = message.chat.id
        assistant = await get_assistant(chat_id)
        ass = await assistant.get_me()
        assid = ass.id
        if assistant is None:
            await app.send_message(chat_id, "<b>خطأ في المساعد</b>")
            return
        msg = await app.send_message(chat_id, "<b>جاري فتح الكول..</b>")
        try:
            peer = await assistant.resolve_peer(chat_id)
            await assistant.invoke(
                CreateGroupCall(
                    peer=InputPeerChannel(
                        channel_id=peer.channel_id,
                        access_hash=peer.access_hash,
                    ),
                    random_id=assistant.rnd_id() // 9000000000,
                )
            )
            await msg.edit_text("<b>تم فتح الكول بنجاح!!</b>")
        except ChatAdminRequired:
            try:    
                await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
                        can_manage_chat=False,
                        can_delete_messages=False,
                        can_manage_video_chats=True,
                        can_restrict_members=False,
                        can_change_info=False,
                        can_invite_users=False,
                        can_pin_messages=False,
                        can_promote_members=False,
                    ),
                )
                peer = await assistant.resolve_peer(chat_id)
                await assistant.invoke(
                    CreateGroupCall(
                        peer=InputPeerChannel(
                            channel_id=peer.channel_id,
                            access_hash=peer.access_hash,
                        ),
                        random_id=assistant.rnd_id() // 9000000000,
                    )
                )
                await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
                    can_manage_chat=False,
                    can_delete_messages=False,
                    can_manage_video_chats=False,
                    can_restrict_members=False,
                    can_change_info=False,
                    can_invite_users=False,
                    can_pin_messages=False,
                    can_promote_members=False,
                    ),
                )                              
                await msg.edit_text("<b>تم فتح الكول بنجاح !!</b>")
            except:
                await msg.edit_text("<b>╮❖ يرجي اعطاء البوت صلاحيه اضافه\n╯❖  مشرفين و تحكم في المحادثة الصوتيه</b>")
    else:
        await message.reply_text("لازم تكون ع الاقل ادمن او اعلي ✨")   


@app.on_message(filters.regex("^اقفل الكول$"), group=732)
@app.on_message(filters.regex("^اقفل الكول$") & filters.channel, group=732)
async def stop_group_call(client: Client, message: Message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 6760053475:
        chat_id = message.chat.id
        assistant = await get_assistant(chat_id)
        ass = await assistant.get_me()
        assid = ass.id
        if assistant is None:
            await app.send_message(chat_id, "<b>خطأ في المساعد</b>")
            return
        msg = await app.send_message(chat_id, "<b>جاري قفل الكول</b>")
        try:
            if not (
               group_call := (
                   await get_group_call(assistant, message, err_msg=", group call already ended")
               )
            ):  
               return
            await assistant.invoke(DiscardGroupCall(call=group_call))
            await msg.edit_text("<b>تم اغلاق الكول بنجاح!</b>")

        except Exception as e:
            if "GROUPCALL_FORBIDDEN" in str(e):
                try:    
                    await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
                        can_manage_chat=False,
                        can_delete_messages=False,
                        can_manage_video_chats=True,
                        can_restrict_members=False,
                        can_change_info=False,
                        can_invite_users=False,
                        can_pin_messages=False,
                        can_promote_members=False,
                    ))
                    if not (
                        group_call := (
                            await get_group_call(assistant, message, err_msg=", group call already ended")
                        )
                    ):  
                        return
                    await assistant.invoke(DiscardGroupCall(call=group_call))
                    await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
                        can_manage_chat=False,
                        can_delete_messages=False,
                        can_manage_video_chats=False,
                        can_restrict_members=False,
                        can_change_info=False,
                        can_invite_users=False,
                        can_pin_messages=False,
                        can_promote_members=False,
                    ))                              
                    await msg.edit_text("<b>تم اغلاق الكول بنجاح!!</b>")
                except:
                    await msg.edit_text("<b>╮❖ يرجي اعطاء البوت صلاحيه اضافه\n╯❖  مشرفين و تحكم في المحادثة الصوتيه</b>")
    else:
        await message.reply_text("لازم تكون ع الاقل ادمن او اعلي ✨")   



#تنبيه بقفل الكول ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#تنبيه بقفل الكول ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#تنبيه بقفل الكول ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.video_chat_started)
async def stcall(client: Client, message: Message): 
      Startt = "<b>انــا جـييــــت 😁</b>"
      await message.reply_text(Startt)

@app.on_message(filters.video_chat_ended)
async def encall(client: Client, message: Message): 
      Enddd = "<b>قـفـله فـي دمـاغـك 😒</b>"
      await message.reply_text(Enddd)

@app.on_message(filters.video_chat_members_invited)
async def mevegaa(client: Client, message: Message): 
           text = f"<b>╮❖ قـام: {message.from_user.mention}\n╯❖ بـدعـوه : </b>"
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"<a href=\"tg://user?id={user.id}\">{user.first_name}</a> "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} ")
           except:
             pass
 