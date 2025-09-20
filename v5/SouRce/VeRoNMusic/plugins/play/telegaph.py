import os
import asyncio
import httpx
from typing import Optional
from urllib.parse import quote_plus
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from VeRoNMusic import app

def get_file_id(msg: Message) -> Optional[Message]:
    if not msg.media:
        return None

    for message_type in ("photo", "animation", "audio", "document", "video", "video_note", "voice", "sticker"):
        obj = getattr(msg, message_type)
        if obj:
            setattr(obj, "message_type", message_type)
            return obj

@app.on_message(filters.command(["تليجراف", "تلكراف", "تلجراف", "تلغراف"], prefixes=""), group=685497235)
async def uguu_upload(bot, update):
    replied = update.reply_to_message
    if not replied:
        return await update.reply_text("🗯︙ يرجى الرد على صورة أو فيديو (حجم أقل من 10MB)")

    file_info = get_file_id(replied)
    if not file_info:
        return await update.reply_text("⚠︙ هذا النوع غير مدعوم!")

    text = await update.reply_text("⬇︙ جاري التحميل إلى الخادم...")
    media = await replied.download()

    await text.edit_text("📤︙ جاري الرفع  ...")

    try:
        async with httpx.AsyncClient() as client:
            with open(media, "rb") as file:
                response = await client.post(
                    "https://uguu.se/api.php?d=upload",
                    files={"file": (os.path.basename(media), file)}
                )
                response.raise_for_status()
                url = response.text.strip()

       
                if not url.startswith(("http://", "https://")):
                    url = f"https://{url}"

               
                encoded_url = quote_plus(url)

    except Exception as e:
        await text.edit_text(f"❌︙ خطأ في الرفع: {str(e)}")
        return

    finally:
        try:
            os.remove(media)
        except:
            pass

    await text.edit_text(
        f"**🎯︙ تم إنشاء الرابط بنجاح:**\n\n{url}",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("‹ 𝖮𝗉𝖾𝗇 ›", url=url),
                InlineKeyboardButton("‹ 𝖲𝗁𝖺𝗋𝖾 ›", url=f"https://t.me/share/url?url={encoded_url}")
            ],
            [
                InlineKeyboardButton("‹ 𝖢𝗅𝗈𝗌𝖾 ›", callback_data="close")
            ]
        ])
    )