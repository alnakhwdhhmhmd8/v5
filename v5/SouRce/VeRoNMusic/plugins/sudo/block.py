from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from VeRoNMusic import app
from VeRoNMusic.misc import SUDOERS
from VeRoNMusic.utils.database import add_gban_user, remove_gban_user
from VeRoNMusic.utils.decorators.language import language

# Command
BLOCK_COMMAND = get_command("BLOCK_COMMAND")
UNBLOCK_COMMAND = get_command("UNBLOCK_COMMAND")
BLOCKED_COMMAND = get_command("BLOCKED_COMMAND")

@app.on_message(filters.command(["حظرر من فيرون"], "") & SUDOERS, group=4)
@app.on_message(filters.command(BLOCK_COMMAND) & SUDOERS)
@language
async def useradd(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if user.id in BANNED_USERS:
            return await message.reply_text(_["block_1"].format(user.mention))
        await add_gban_user(user.id)
        BANNED_USERS.add(user.id)
        await message.reply_text(_["block_2"].format(user.mention))
        return
    if message.reply_to_message.from_user.id in BANNED_USERS:
        return await message.reply_text(
            _["block_1"].format(message.reply_to_message.from_user.mention)
        )
    await add_gban_user(message.reply_to_message.from_user.id)
    BANNED_USERS.add(message.reply_to_message.from_user.id)
    await message.reply_text(
        _["block_2"].format(message.reply_to_message.from_user.mention)
    )

@app.on_message(filters.command(["فك حظر من فيرون"], "") & SUDOERS, group=654)
@app.on_message(filters.command(UNBLOCK_COMMAND) & SUDOERS)
@language
async def userdel(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if user.id not in BANNED_USERS:
            return await message.reply_text(_["block_3"])
        await remove_gban_user(user.id)
        BANNED_USERS.remove(user.id)
        await message.reply_text(_["block_4"])
        return
    user_id = message.reply_to_message.from_user.id
    if user_id not in BANNED_USERS:
        return await message.reply_text(_["block_3"])
    await remove_gban_user(user_id)
    BANNED_USERS.remove(user_id)
    await message.reply_text(_["block_4"])

@app.on_message(filters.command(["الممنوعين"], "") & SUDOERS, group=4)
@app.on_message(filters.command(BLOCKED_COMMAND) & SUDOERS)
@language
async def sudoers_list(client, message: Message, _):
    if not BANNED_USERS:
        return await message.reply_text(_["block_5"])
    mystic = await message.reply_text(_["block_6"])
    msg = _["block_7"]
    count = 0
    for users in BANNED_USERS:
        try:
            user = await app.get_users(users)
            user = user.first_name if not user.mention else user.mention
            count += 1
        except Exception:
            continue
        msg += f"{count}➤ {user}\n"
    if count == 0:
        return await mystic.edit_text(_["block_5"])
    else:
        return await mystic.edit_text(msg)


__MODULE__ = "B-ʟɪsᴛ"
__HELP__ = """
<u><b><blockquote> اوامر الطرد والحظر :</b></blockquote><blockquote>

╮❖  تقييد /restrict
│᚜❖ حظر /ban 
│᚜❖ كتم /mute
│᚜❖ الغاء الحظر /Unblock
│᚜❖ طرد البوتات /Blockbots
│᚜❖ الغاء الكتم /Unmute
│᚜❖ حظر الجروب : /blacklistchat
│᚜❖ الغاء حظر الحروب : /whitelistchat
│᚜❖ الجروبات المحظور : /blacklistedchat
╯❖  الغاء التقييد /Unsubscribe
</blockquote><blockquote><u><b>اوامر الرفع و تنزيل:</b></u></blockquote><blockquote>
 
╮❖  رفع مالك /Raiseowner
│᚜❖ رفع ادمن : /Adminup
│᚜❖ رفع مطور : /Devup
│᚜❖ تنزيل مطور : /UnDev
│᚜❖ تنزيل مالك : /Unowner
╯❖  تنزيل ادمن :/UnAdmin

 </blockquote><blockquote><b>لظهار قوائم:</b></u></blockquote><blockquote>
 
╮❖  قائمة المكتومين
│᚜❖ قائمة المحظورين
│᚜❖ قائمة المقيدين
│᚜❖ قائمة المطورين
│᚜❖ قائمة المالكين
│᚜❖ قائمة المشرفين
╯❖  قائمة الادمنيه

</blockquote><blockquote><u><b>اوامر المسح :</b></blockquote><blockquote>

╮❖  مسح الادمنيه
│᚜❖ مسح المحظورين
│᚜❖ مسح المكتومين
│᚜❖ مسح المقيدين
│᚜❖ مسح المالكين
│᚜❖ مسح الادمنيه
╯❖  مسح المطورين 
</blockquote>
</b>
"""