from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from VeRoNMusic import app
import random
import aiohttp
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

iddof = []

@app.on_message(filters.command(["زوجني", "ز"], prefixes=["/", ".", ""]) & filters.group, group=7952)
async def idddf(client, message):
    global iddof

    chat_id = message.chat.id
    if chat_id in iddof:
        return
    
    members = []
    async for member in client.get_chat_members(chat_id):
        if not member.user.is_bot:
            members.append(member)
    
    if not members:
        await client.send_message(chat_id, "لا يوجد أعضاء غير بوتات في هذه الدردشة.")
        return
    
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    
    random_message = f"💞 جبتلك عروسة لقطة {random_member_mention} ايه رأيك؟"
    
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("💍 موافق", callback_data=f"accept_{random_member.user.id}"),
                InlineKeyboardButton("🙅‍♂️ مش موافق", callback_data=f"reject_{random_member.user.id}")
            ]
        ]
    )
    
    await client.send_message(chat_id, random_message, reply_markup=keyboard)
    iddof.append(chat_id)

async def get_user_photo(client, user_id):
    photos = await client.get_profile_photos(user_id, limit=1)
    if photos.total_count > 0:
        file = await client.download_media(photos.photos[0].file_id)
        return file
    return None

async def create_marriage_image(user1_photo, user2_photo, user1_name, user2_name):
    # تحميل الإطار الجديد بدقة
    async with aiohttp.ClientSession() as session:
        async with session.get("https://h.uguu.se/CPEXuvPQ.jpg") as resp:
            frame_bytes = await resp.read()

    frame = Image.open(BytesIO(frame_bytes)).convert("RGBA")

    # فتح صور المستخدمين وتعديل حجمها
    user1_img = Image.open(user1_photo).convert("RGBA").resize((400, 400))
    user2_img = Image.open(user2_photo).convert("RGBA").resize((400, 400))

    # لصق الصور في أماكنها بدقة
    frame.paste(user1_img, (150, 280), user1_img)
    frame.paste(user2_img, (900, 280), user2_img)

    # إضافة أسماء المستخدمين أسفل الصور
    draw = ImageDraw.Draw(frame)
    try:
        font = ImageFont.truetype("arial.ttf", size=48)
    except:
        font = ImageFont.load_default()

    draw.text((200, 580), user1_name, fill="black", font=font)
    draw.text((950, 580), user2_name, fill="black", font=font)

    output = BytesIO()
    frame.save(output, format='PNG')
    output.seek(0)
    return output

@app.on_callback_query()
async def callback_query(client, callback_query):
    data = callback_query.data.split("_")
    if len(data) != 2 or not data[1].isdigit():
        await callback_query.answer("حدث خطأ. البيانات غير صالحة.", show_alert=True)
        return
    
    action = data[0]
    user_id = int(data[1])
    chat_id = callback_query.message.chat.id
    
    if action == "accept":
        user1_id = callback_query.from_user.id
        user2_id = user_id
        
        user1_photo = await get_user_photo(client, user1_id)
        user2_photo = await get_user_photo(client, user2_id)
        
        if user1_photo and user2_photo:
            user1_name = callback_query.from_user.first_name
            user2 = await client.get_users(user2_id)
            user2_name = user2.first_name

            marriage_image = await create_marriage_image(user1_photo, user2_photo, user1_name, user2_name)
            await client.send_photo(chat_id, marriage_image, caption=f"🥳 مبروك الزواج بين {user1_name} و {user2_name}!")
        else:
            await client.send_message(chat_id, "🥲 لم أتمكن من تحميل صوركم. تأكدوا أن لديكم صور بروفايل.")

    elif action == "reject":
        await client.send_message(chat_id, "🙃 اممم طيب مين تاني؟")
    else:
        await callback_query.answer("خيار غير معروف.", show_alert=True)

