from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from VeRoNMusic import app
import random

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
    
    random_message = f"جبتلك عروسة انما ايه لقطة {random_member_mention} ايه رأيك فيها؟؟"
    
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("موافق", callback_data=f"accept_{random_member.user.id}"),
                InlineKeyboardButton("مش موافق", callback_data=f"reject_{random_member.user.id}")
            ]
        ]
    )
    
    await client.send_message(chat_id, random_message, reply_markup=keyboard)
    iddof.append(chat_id)


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
        user_mention = f"[{callback_query.from_user.first_name}](tg://user?id={callback_query.from_user.id})"
        await client.send_message(chat_id, f"مبروك عليكم تم زواجك من {user_mention}.")
    elif action == "reject":
        await client.send_message(chat_id, "امال عاوزني اجبلك مين تتجوزه؟")
    else:
        await callback_query.answer("خيار غير معروف.", show_alert=True)

if __name__ == "__main__":
    app.run()