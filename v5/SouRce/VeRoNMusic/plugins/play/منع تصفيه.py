from pyrogram import filters
from pyrogram.types import ChatMemberUpdated
from collections import defaultdict
from VeRoNMusic import app  # بوتك الأساسي

# عداد الطرد لكل مشرف
kick_counter = defaultdict(int)
kick_limit = 3

@app.on_chat_member_updated(filters.group)
async def protect_group(client, update: ChatMemberUpdated):
    if update.new_chat_member.status == "kicked" and update.old_chat_member.status in ["member", "restricted"]:
        if not update.from_user:
            return  # تجاهل إذا لم نعرف من قام بالطرد

        kicker_id = update.from_user.id
        chat_id = update.chat.id

        # تحقق أن الشخص الذي قام بالطرد هو مشرف
        kicker = await client.get_chat_member(chat_id, kicker_id)
        if kicker.status in ["administrator", "creator"]:
            kick_counter[(chat_id, kicker_id)] += 1
            count = kick_counter[(chat_id, kicker_id)]

            print(f"[🚨 حماية] {kicker.user.first_name} قام بطرد عضو ({count}/{kick_limit})")

            if count >= kick_limit:
                # إزالة صلاحيات المشرف
                await client.promote_chat_member(
                    chat_id,
                    kicker_id,
                    can_change_info=False,
                    can_post_messages=False,
                    can_edit_messages=False,
                    can_delete_messages=False,
                    can_invite_users=False,
                    can_restrict_members=False,
                    can_pin_messages=False,
                    can_promote_members=False,
                    can_manage_video_chats=False
                )
                await client.send_message(chat_id, f"🚨 تم إنزال {kicker.user.first_name} من المشرفين لأنه طرد {kick_limit} أعضاء.")
                kick_counter[(chat_id, kicker_id)] = 0  # إعادة العداد