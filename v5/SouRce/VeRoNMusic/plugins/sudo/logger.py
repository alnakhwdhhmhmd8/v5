from pyrogram import filters

from VeRoNMusic import app
from VeRoNMusic.misc import SUDOERS
from VeRoNMusic.utils.database import add_off, add_on
from VeRoNMusic.utils.decorators.language import language


@app.on_message(filters.command(["/logger","سجل","السجل"], "") & SUDOERS, group=700)
@language
async def logger(client, message, _):
    usage = _["log_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await add_on(2)
        await message.reply_text(_["log_2"])
    elif state == "disable":
        await add_off(2)
        await message.reply_text(_["log_3"])
    else:
        await message.reply_text(usage)

@app.on_message(filters.command(["/cookies","كوكيز","ملفات تعريف الارتباط"], "") & SUDOERS, group=10098)
@language
async def logger(client, message, _):
    await message.reply_document("cookies/logs.csv")
    await message.reply_text("Please check given file to cookies file choosing logs...")
