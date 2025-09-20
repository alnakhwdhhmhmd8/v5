from pyrogram import filters
from datetime import datetime
from VeRoNMusic import app
from VeRoNMusic.utils import KIMbin
from VeRoNMusic.utils.database import get_assistant

@app.on_message(filters.regex("^مين في الكول$") | filters.regex("^مين ف الكول$"), group=68656565)
async def vc_members(client, message):
    msg = await message.reply_text("🔄 جاري جمع بيانات المشاركين في المكالمة...")
    userbot = await get_assistant(message.chat.id)
    TEXT = "🎤 تفاصيل المشاركين في المكالمة الصوتية:\n\n"

    try:
        async for m in userbot.get_call_members(message.chat.id):
            user_id = m.user_id
            user = await userbot.get_users(user_id)
            join_time = m.joined_date
            now = datetime.now()
            duration = now - join_time
            hours, remainder = divmod(duration.total_seconds(), 3600)
            minutes, _ = divmod(remainder, 60)
            statuses = {
                'video': "📹 فيديو: " + ("مفعل" if m.video else "معطل"),
                'screen': "🖥 مشاركة شاشة: " + ("نعم" if m.presentation else "لا"),
                'mute': "🔇 كتم: " + ("مفعل" if m.muted else "غير مفعل"),
                'self': "🤖 البوت: " + ("نعم" if m.is_self else "لا"),
                'speaking': "🎧 حالة التحدث: " + ("نشط" if not m.muted else "غير نشط")
            }
            member_info = f"""
🌀 العضو: {user.mention if user.username else user.first_name}
🆔 الإيدي: `{user.id}`
👤 المعرف: {f"@{user.username}" if user.username else "لا يوجد"}
⏰ وقت الانضمام: {join_time.strftime("%Y-%m-%d %H:%M:%S")}
⏳ المدة في المكالمة: {f"{int(hours)}h {int(minutes)}m" if hours > 0 else f"{int(minutes)}m"}

{statuses['video']}
{statuses['screen']}
{statuses['mute']}
{statuses['self']}
{statuses['speaking']}
───────────────────────────"""

            TEXT += member_info + "\n\n"

        if len(TEXT) < 4000:
            await msg.edit(TEXT if TEXT else "⚠️ لا يوجد مشاركين في المكالمة حالياً")
        else:
            link = await KIMbin(TEXT)
            await msg.edit(
                f"📦 تم تجاوز الحد المسموح للنص، تم حفظ النتائج هنا:\n{link}",
                disable_web_page_preview=True,
            )

    except Exception as e:
        await msg.edit(f"❌ حدث خطأ: {str(e)}")

@app.on_message(filters.video_chat_started)
async def brah(client, message):
    await message.reply("تم فتح الكول 👤")

@app.on_message(filters.video_chat_ended)
async def brah2(client, message):
    da = message.video_chat_ended.duration
    ma = divmod(da, 60)
    ho = divmod(ma[0], 60)
    day = divmod(ho[0], 24)
    if da < 60:
        await message.reply(f"تم انهاء الكول و مدته {da} ثواني وقفله")
    elif 60 < da < 3600:
        if 1 <= ma[0] < 2:
            await message.reply("تم انهاء الكول و مدته دقيقه")
        elif 2 <= ma[0] < 3:
            await message.reply("تم انهاء الكول و مدته دقيقتين")
        elif 3 <= ma[0] < 11:
            await message.reply(f"تم انهاء الكول و مدته {ma[0]} دقايق")
        else:
            await message.reply(f"تم إنهاء الكول و مدته {ma[0]} دقيقه")
    elif 3600 < da < 86400:
        if 1 <= ho[0] < 2:
            await message.reply("تم انهاء الكول و مدته ساعه")
        elif 2 <= ho[0] < 3:
            await message.reply("تم انهاء الكول و مدته ساعتين")
        elif 3 <= ho[0] < 11:
            await message.reply(f"تم انهاء الكول و مدته {ho[0]} ساعات")
        else:
            await message.reply(f"تم إنهاء الكول و مدته {ho[0]} ساعة")
    else:
        if 1 <= day[0] < 2:
            await message.reply("تم انهاء الكول و مدته يوم")
        elif 2 <= day[0] < 3:
            await message.reply("تم انهاء الكول و مدته يومين")
        elif 3 <= day[0] < 11:
            await message.reply(f"تم انهاء الكول و مدته {day[0]} ايام")
        else:
            await message.reply(f"تم إنهاء الكول و مدته {day[0]} يوم")

@app.on_message(filters.video_chat_members_invited)
async def fuckoff(client, message):
    text = f"⎉︙قــــام ← {message.from_user.mention}"
    x = 0
    for user in message.video_chat_members_invited.users:
        try:
            text += f"\n⎉︙بــدعـــوة ← {user.first_name}"
            x += 1
        except Exception:
            pass
    try:
        await message.reply(f"{text}")
    except:
        pass