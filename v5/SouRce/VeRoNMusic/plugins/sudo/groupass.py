from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, LOG_GROUP_ID
from VeRoNMusic import app
from VeRoNMusic.core.userbot import assistants
from VeRoNMusic.utils.assistant import get_assistant_details
from VeRoNMusic.utils.assistant import is_avl_assistant as assistant
from VeRoNMusic.utils.database import get_assistant, save_assistant, set_assistant
from VeRoNMusic.utils.decorators import AdminActual


@app.on_message(filters.command(["تغير المساعد"], "") & ~BANNED_USERS, group=433334)
@AdminActual
async def assis_change(client, message: Message, _):
    if await assistant() == True:
        return await message.reply_text(
            "عذرًا سيدي! في سيرفر البوت هناك مساعد واحد فقط متاح لذلك لا يمكنك تغيير المساعد"
        )
    usage = f"**تم اكتشاف استخدام خاطئ للأمر\n**الاستخدام:**\n/تغيير_المساعد - لتغيير مساعد مجموعتك الحالي إلى مساعد عشوائي في سيرفر البوت"
    if len(message.command) > 2:
        return await message.reply_text(usage)
    a = await get_assistant(message.chat.id)
    DETAILS = f"تم تغيير مساعد دردشتك من [{a.name}](https://t.me/{a.username}) "
    if not message.chat.id == LOG_GROUP_ID:
        try:
            await a.leave_chat(message.chat.id)
        except:
            pass
    b = await set_assistant(message.chat.id)
    DETAILS += f"إلى [{b.name}](https://t.me/{b.username})"
    try:
        await b.join_chat(message.chat.id)
    except:
        pass
    await message.reply_text(DETAILS, disable_web_page_preview=True)


@app.on_message(filters.command(["تعيين المساعد"], "") & ~BANNED_USERS, group=65555)
@AdminActual
async def assis_set(client, message: Message, _):
    if await assistant():
        return await message.reply_text(
            "عذرًا سيدي! في سيرفر البوت هناك مساعد واحد فقط متاح لذلك لا يمكنك تغيير المساعد"
        )
    usage = await get_assistant_details()
    if len(message.command) != 2:
        return await message.reply_text(usage, disable_web_page_preview=True)
    query = message.text.split(None, 1)[1].strip()
    if query not in assistants:
        return await message.reply_text(usage, disable_web_page_preview=True)
    a = await get_assistant(message.chat.id)
    try:
        await a.leave_chat(message.chat.id)
    except:
        pass
    await save_assistant(message.chat.id, query)
    b = await get_assistant(message.chat.id)
    try:
        await b.join_chat(message.chat.id)
    except:
        pass
    await message.reply_text(
        f"**تفاصيل المساعد الجديد لدردشتك:**\nاسم المساعد :- {b.name}\nاسم المستخدم :- @{b.username}\nالايدي:- {b.id}",
        disable_web_page_preview=True,
    )


@app.on_message(filters.command(["معلومات المساعد"], "") & filters.group & ~BANNED_USERS, group=65444)
@AdminActual
async def check_ass(client, message: Message, _):
    a = await get_assistant(message.chat.id)
    await message.reply_text(
        f"**تفاصيل مساعد دردشتك:**\nاسم المساعد :- {a.name}\nاسم المستخدم :- @{a.username}\nايدي المساعد:- {a.id}",
        disable_web_page_preview=True,
    )