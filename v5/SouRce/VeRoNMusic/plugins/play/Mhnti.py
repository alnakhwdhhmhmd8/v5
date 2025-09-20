import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from VeRoNMusic import app

@app.on_message(filters.command(['مهنتي'], prefixes="") & filters.group, group=673487)
async def get_user_info(client, message):
    # إعداد رابط البروفايل
    username = message.from_user.username
    if username:
        url = f"https://t.me/{username}"
    else:
        url = "https://t.me/Source_Veron"

    # معلومات عشوائية
    age = random.randint(20, 30)
    jobs = ["مدرس 👨‍🏫", "طبيب 👨‍⚕", "مهندس 👷‍♂", "خيال 🏇", "سباح 🏊", "مطور 👨‍💻"]
    job = random.choice(jobs)
    statuses = ["متزوج 👨‍👩‍👧‍👦", "اعزب 🧍‍♂", "مرتبط 👩‍❤️‍💋‍👨", "نرجسي 💆‍♂", "ملهم 🧝‍♂"]
    status = random.choice(statuses)

    # إعداد الأزرار
    inline_keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(f"↢ اسمك :  {message.from_user.first_name}", url=url)],
            [InlineKeyboardButton(f"↢ عمرك :  {age}", callback_data=f"age_{age}")],
            [InlineKeyboardButton(f"↢ مهنتك :  {job}", callback_data=f"job_{job}")],
            [InlineKeyboardButton(f"↢ حالتي :  {status}", callback_data=f"status_{status}")],
            [InlineKeyboardButton("𝖲𝗈𝖴𝗋𝖼𝖾 VeRoN", url="https://t.me/Source_Veron")]
        ]
    )

    # رابط صورة عشوائية (تأكد من استبداله برابط حقيقي)
    photo_url = "https://d.uguu.se/yCwrXfeu.jpg"

    # إرسال الرسالة بالصورة والأزرار
    await client.send_photo(
        chat_id=message.chat.id,
        photo=photo_url,
        caption="هذه معلوماتك العشوائية:",
        reply_markup=inline_keyboard
    )