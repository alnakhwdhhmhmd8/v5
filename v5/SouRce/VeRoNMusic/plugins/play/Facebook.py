
import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from VeRoNMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from VeRoNMusic import app
from random import  choice, randint



@app.on_message(filters.command(["فيسبوك","فيس بوك","فيس","Facebook"], ""), group=668)
async def facebook(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://h.uguu.se/dFgLyqTz.jpg",
        caption=f"""**<b>[سوࢪس فيࢪوטּ | 𝙎𝙤𝙪𝙧𝙘𝙚 𝙑𝙚𝙧𝙤𝙣. #]</u>\nيمكنك إنشاء حساب أو تسجيل الدخول\n إلى فيسبوك والتواصل مع الأصدقاء وأفراد العائلة والأشخاص الآخرين\n الذين تعرفهم. استمتع بمشاركة الصور ومقاطع الفيديو**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ғᴀᴄᴇ»ʙᴏᴏᴋ", url=f"https://m.facebook.com"), 
                 ],[
                    InlineKeyboardButton(
                        "ᴠᴇʀᴏɴ", url=f"https://t.me/Source_Veron"),
                ],

            ]

        ),

    )
    
    
    

@app.on_message(filters.command(["انستا","انستغرام","انستاجرام","Instagram"], ""), group=400)
async def agram(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://n.uguu.se/oqYXPJaJ.jpg",
        caption=f"""**✘<u>⸢ᴠᴇʀᴏɴダ⸢ɪɴsᴛᴀɢʀᴀᴍ♪⸥ :</u>\nشارك كل تفاصيل حياتك\nوصورك و فيدوهاتك مع جميع\nاصدقائك لحظه بلحظه**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ɪɴsᴛᴀɢʀᴀᴍ", url=f"https://Instagram.com"), 
                 ],[
                    InlineKeyboardButton(
                        "ᴠᴇʀᴏɴ", url=f"https://t.me/Source_Veron"),
                ],

            ]

        ),

    )    







@app.on_message(filters.command(["تويتر","تغريد","تغريده","Twitter"], ""), group=300)
async def Twitter(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://d.uguu.se/SkHKxdjG.jpg",
        caption=f"""**✘<u>⸢ᴠᴇʀᴏɴダ⸢𝘁𝘄𝗶𝘁𝘁𝗲𝗿♪⸥ :</u>\nنضم إلى المحادثة! تويتر هو من أفضل تطبيقات\n السوشيال ميديا والأخبار حيث يأخذك إلى\n قلب الحدث، بداية من أخبار العالم وأخبار\n العالم العربي، وحالة الطقس ...**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 𝘁𝘄𝗶𝘁𝘁𝗲𝗿 ", url=f"https://Twitter.com"), 
                 ],[
                    InlineKeyboardButton(
                        "ᴠᴇʀᴏɴ", url=f"https://t.me/Source_Veron"),
                ],

            ]

        ),

    )    







@app.on_message(filters.command(["يوتيوب","يوت","فيديوها","Youtube"], ""), group=600)
async def Youtube(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://h.uguu.se/neopJaWD.jpg",
        caption=f"""**✘<u>⸢ᴠᴇʀᴏɴダ⸢𝐘𝐨𝐮𝐓𝐮𝐛𝐞♪⸥ :</u>\n
يمكنك الاستمتاع بالفيديوهات والموسيقى التي تحبها \nوتحميل المحتوى الأصلي ومشاركته بكامله مع\n أصدقائك وأفراد عائلتك والعالم أجمع على **""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 𝐘𝐨𝐮𝐓𝐮𝐛𝐞 ", url=f"https://Youtube.com"), 
                 ],[
                    InlineKeyboardButton(
                        "ᴠᴇʀᴏɴ", url=f"https://t.me/Source_Veron"),
                ],

            ]

        ),

    )    
    




@app.on_message(filters.command(["البوت فازر","botfather","فازر"], ""), group=200)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f92e2bea944757b09adb1.jpg",
        caption=f"""**⋖━⦿═⊷⋆父ᴠᴇʀᴏɴ父⋆⊷═⦿━⋗**\n\nها اهلايٕن عمـٕري {message.from_user.mention}❄️\n\nفي بوت فازر لانشاء بوتك تابع الازرار\n\n**⋖━⦿═⊷⋆父ᴠᴇʀᴏɴ父⋆⊷═⦿━⋗**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ʙᴏᴛ.ғᴀᴛʜᴇʀ", url=f"https://t.me/BotFather"), 
                 ],[
                    InlineKeyboardButton(
                        "ᴠᴇʀᴏɴ", url=f"https://t.me/Source_Veron"),
                ],

            ]

        ),

    )






@app.on_message(filters.command(["شات جي بي دي","اذكاء الاصطناعي","ChatGPT","g"], ""), group=220)
async def hudsaqhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://h.uguu.se/nxRCDfpn.jpg",
        caption=f"""**⋖━⦿═⊷⋆父ᴠᴇʀᴏɴ父⋆⊷═⦿━⋗**\n\nها اهلايٕن عمـٕري {message.from_user.mention}❄️\nفي اذكاء الاصطناعي من سورس فيࢪون\nيمكن تحدث الي او حل مشكلتك\nاو عمل اي شي تريده\nفقت قم بارسال /gpt ومرفق معه سؤالك\n\n**⋖━⦿═⊷⋆父ᴠᴇʀᴏɴ父⋆⊷═⦿━⋗**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴠᴇʀᴏɴ", url=f"https://t.me/Source_Veron"),
                ],

            ]

        ),

    )







                
@app.on_message(filters.command(["بوت حذف"], ""), group=2230)
async def huhcw(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/75ccc1c74567c6e36f640.jpg",
        caption=f"""**⋖━⦿═⊷〩ᴠᴇʀᴏɴ々ᴍᴜsɪᴄ〩⊷⦿━⋗**\n\nها اهلايٕن عمـٕري {message.from_user.mention}❄️\nرايح تحذف ليه يا ارنيوبي\nزهقت مننا ولا ايه\nطب يلا مع الف داهيه🥹😂\n\n**⋖━⦿═⊷〩ᴠᴇʀᴏɴ々ᴍᴜsɪᴄ〩⊷⦿━⋗**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "في ستين داهيه", url=f"https://t.me/LC6BOT"), 
                 ],[
                    InlineKeyboardButton(
                        "ᴠᴇʀᴏɴ", url=f"https://t.me/Source_Veron"),
                ],

            ]

        ),

    )




@app.on_message(filters.command(["المميز","تلي مميز","مميز"], ""), group=4890)
async def hfwfuhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/65c2c3cf294223da44d3c.jpg",
        caption=f"""**⋖━⦿═⊷〩ᴠᴇʀᴏɴ々ᴍᴜsɪᴄ〩⊷⦿━⋗**\n\nها اهلايٕن عمـٕري {message.from_user.mention}\nالانطلاق إلى ماوراء الحدود والحصول على مزايا حصريّة\nوالمساهمة في دعم تطوير تيليجرام بالاشتراك في تيليجرام المُميّز.\n\n**⋖━⦿═⊷〩ᴠᴇʀᴏɴ々ᴍᴜsɪᴄ〩⊷⦿━⋗**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴘʀᴇᴍɪᴜᴍ⸢ʙᴏᴛ⸥", url=f"https://t.me/PremiumBot"), 
                 ],[
                    InlineKeyboardButton(
                        "ᴠᴇʀᴏɴ", url=f"https://t.me/Source_Veron"),
                ],

            ]

        ),

    )
        