import os
import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
import pymongo
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from time import sleep
from bot import DEVELOPERS
import pymongo

# الإعدادات الأساسية
API_ID = int("20551716")  # أي دي التطبيق
API_HASH = "564355da021dc5739c01f33fb015eaf1"  # هاش التطبيق
BOTS_LIST = []  # قائمة تخزن البوتات المصنوعة [يوزر البوت, أي دي المطور]
SERVICE_ACTIVE = True  # حالة المجاني (تفعيل/تعطيل)
CHANNEL = "Source_VeRoN"  # قناة السورس الإجبارية
DEVELOPERS = ["ToxVe","TopVeGa"]  # قائمة المطورين
mongo = pymongo.MongoClient("mongodb+srv://kuldiprathod2003:kuldiprathod2003@cluster0.wxqpikp.mongodb.net/?retryWrites=true&w=majority")
db = mongo["KIM"]["BO6262TtS_LIST"]

## ----- الوظائف المساعدة ----- ##

# للتحقق من اشتراك المستخدم في القناة
@Client.on_message(filters.private)
async def check_subscription(client, message):
    if not SERVICE_ACTIVE and message.from_user.username not in SUDOERS:
        return await message.reply_video(
            video="https://h.uguu.se/NuRwKkaV.mp4",
            caption=f"⌯︙عذࢪاَ عزيزي {message.from_user.mention}\n"
                    "\n⌯︙الوضع المجاني معطل حـاليا"
                    "\n⌯︙راسل المطور لي التنصيب المدفوع"
                    "\n⌯︙Dev : @ToxVe" 
                    "ꔹ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ꔹ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("◜ꪔY ժᥱ᥎◞", url="https://t.me/ToxVe")]
                ]
            )
        )
    
    try:
        await client.get_chat_member(CHANNEL, message.from_user.id)
    except Exception:
        return await message.reply_video(
            video="https://h.uguu.se/NuRwKkaV.mp4",
            caption=f"⌯︙عذࢪاَ عزيزي {message.from_user.mention}\n"
                    "⌯︙عـليك الاشـتࢪاك في قنـاة البـوت اولآ\n"
                    "⌯︙قناة السورس: @Source_Veron\n" 
                    "ꔹ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ꔹ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("𝑪𝒉𝒂𝒏𝒂𝒍 𝑺𝒐𝒖𝒓𝒄𝒆", url=f"https://t.me/{CHANNEL}")]
                ]
            )
        )
    message.continue_propagation()
## ----- أوامر البوت ----- ##


@Client.on_message(filters.command(["السورس"], ""))
async def show_source(client: Client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("𝑮𝒓𝒐𝒖𝒑 𝑺𝒖𝒑𝒑𝒐𝒓𝒕", url="https://t.me/Suport_Veron"),
            InlineKeyboardButton("𝑪𝒉𝒂𝒏𝒂𝒍 𝑺𝒐𝒖𝒓𝒄𝒆", url="https://t.me/Source_Veron"),
        ],
        [
            InlineKeyboardButton("◜ꪔY ժᥱ᥎◞", url="https://t.me/ToxVe")
        ]
    ])

    await message.reply_photo(
        photo="https://d.uguu.se/yCwrXfeu.jpg",
        caption="• مـرحبـا في الصـانع الخـاص بسـورس فيࢪون\n— — — — — — — — —\n• مـبرمج السـورس : @ToxVe\n• قنـاة السـورس : @Source_Veron\nاذا اردت تنصيب بوت ميوزك قـم بالضغط عـلي زر اصنع بوت بالاسفل واتبع الخطوات كما هو موضح لك",
        reply_markup=keyboard,
    )



					


@Client.on_message(filters.command(["تفعيل المجاني", "تعطيل المجاني"], "") & filters.private)
async def toggle_service(client, message):
    if message.from_user.username not in DEVELOPERS:
        return
    global SERVICE_ACTIVE
    SERVICE_ACTIVE = message.text == "تفعيل المجاني"
    status = "مفعّلة" if SERVICE_ACTIVE else "معطّلة"
    await message.reply_text(f"تم {status} المجاني بنجاح")

## ----- إدارة البوتات ----- ##
@Client.on_message(filters.command("صنع بوت", "") & filters.private)
async def Files(client, message):
    if message.from_user.username not in DEVELOPERS:
        for x in BOTS_LIST:
            if int(x[1]) == message.from_user.id:
                return await message.reply_text("لـقد قمـت بـصنـع بـوت مـن قـبـل")
    try:
        ask = await client.ask(message.chat.id, "⎆ أرسل توكن البوت من @BotFather\n\n ♲ يمكنك إيقاف العملية بإرسال /cancel", timeout=300)
    except:
        return
    TOKEN = ask.text
    try:
        ask = await client.ask(message.chat.id, "⎆ بعد إنشاء الجلسة من @PU1_bot، أرسلها هنا:\n\n ♲ يمكنك إلغاء العملية بإرسال /cancel", timeout=300)
    except:
        return
    SESSION = ask.text
    if message.from_user.username in DEVELOPERS:
        try:
            ask = await client.ask(message.chat.id, "⎆ أرسل أي دي المطور (رقم فقط):", timeout=300)
            Dev = int(ask.text)
        except:
            return await message.reply_text("قم بارسال الايدي بشكل صحيح")
    else:
        Dev = message.from_user.id
    bot = Client(":memory:", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN, in_memory=True)
    user = Client("zero", api_id=API_ID, api_hash=API_HASH, session_string=str(SESSION), test_mode=True, in_memory=True)
    try:
        await bot.start()
        username = await bot.get_me()
        username = username.username
        await bot.stop()
        await user.start()
        await user.stop()
    except:
        return await message.reply_text("عـزيزي تـاكد مـن تـوكن و جـلسـه")
    id = username
    for x in BOTS_LIST:
        if x[0] == id:
            return await message.reply_text("لقد قمت بصنع هذا البوت من قبل ")
    os.system(f"cp -a SouRce Files/{id}")
    env = open(f"Files/{id}/.env", "w+", encoding="utf-8")
    x = f'ID = {id}\nBOT_TOKEN = {TOKEN}\nSTRING_SESSION = {SESSION}\nOWNER_ID = {Dev}\nLOG_GROUP_ID = {Dev}'
    env.write(x)
    env.close()
    os.system(f"cd Files/{id} && chmod +x * && screen -d -m -S {id} python3 -m VeRoNMusic")
    oo = [id, Dev]
    BOTS_LIST.append(oo)
    for chat in DEVELOPERS:
        try:
            await client.send_message(chat, f"<b>تـم دخـول بـوت جديد الي فيࢪون\n\n╭⦿ᚐ⸢ᴜsᴇꝛ ʙᴏᴛ⸥» @{id}\n╰⦿ᚐ⸢ᴛᴏᴋᴇɴ⸥ » `{TOKEN}`\n\n⸢˹sᴛꝛɪɴɢ✗ᴩʏꝛᴏɢꝛᴧᴍ : {pyrover}\n <code>{SESSION}</code> \n\n╭⦿ᚐ⸢ᴏᴡɴᴇꝛ⸥» {message.from_user.mention}\n╰⦿ᚐ⸢ᴏᴡɴᴇꝛ ɪᴅ⸥ » <code>{Dev}</code></b>")
        except:
            pass
    
    print("New Bot VeRoN♥️")
    data = {"username": id, "dev": Dev}
    db.insert_one(data)
    await message.reply_text(f"✅ تم إنشاء البوت بنجاح!\n\n ⎆ يوزر البوت: @{id}\n ⎆ أي دي المطور: {Dev}\n\n سيتم تشغيل البوت خلال 1-2 دقيقة")

# حذف بوت
@Client.on_message(filters.command("حذف بوت", "") & filters.private)
async def delete_bot(client, message):
    if message.from_user.username not in DEVELOPERS:
        for bot in BOTS_LIST:
            if bot[1] == message.from_user.id:
                os.system(f"rm -rf Files/{bot[0]}")
                os.system(f"screen -XS {bot[0]} quit")
                BOTS_LIST.remove(bot)
                return await message.reply_text("✅ تم حذف بوتك")
        return await message.reply_text("❌ ليس لديك بوتات لحذفها")
    try:
        bot_msg = await client.ask(message.chat.id, "🔍 أرسل يوزر البوت:", timeout=200)
        bot_username = bot_msg.text.replace("@", "")
    except:
        return await message.reply_text("⏱ انتهى الوقت المحدد")
    for bot in BOTS_LIST:
        if bot[0] == bot_username:
            os.system(f"rm -rf Files/{bot_username}")
            os.system(f"screen -XS {bot_username} quit")
            BOTS_LIST.remove(bot)
            return await message.reply_text("✅ تم حذف البوت بنجاح")

    await message.reply_text("❌ البوت غير موجود")

# عرض البوتات المصنوعة
# عرض البوتات المصنوعة
# عرض البوتات المصنوعة
@Client.on_message(filters.command("قائمة البوتات", ""))
async def list_bots(client, message):
    if message.from_user.username not in DEVELOPERS:
        return await message.reply_text("❌ هذا الأمر متاح فقط للمطورين")
    
    bots = db.find()  # جلب جميع البوتات من قاعدة البيانات
    bots_list = list(bots)
    
    if not bots_list:
        return await message.reply_text("⚠️ لا يوجد بوتات مصنوعة بعد")
    
    text = """ قائمة البوتات المصنوعة
"""
    
    text += f"\nعدد البوتات : {len(bots_list)}\n\n"
    
    for index, bot in enumerate(bots_list, start=1):
        text += f"""<b>{index}- البوت: @{bot["username"]} | معرف المطور: <code>{bot["dev"]}</code>\n"""
    
    await message.reply_text(text, disable_web_page_preview=True)
    
    
    
    
@Client.on_message(filters.command("إحصائيات البوتات", "") & filters.private)
async def bots_stats(client, message):
    if message.from_user.username not in DEVELOPERS:
        return await message.reply_text("❌ هذا الأمر متاح فقط للمطورين")
    
    # جلب جميع البوتات من قاعدة البيانات
    bots = db.find()
    bots_list = list(bots)
    
    if not bots_list:
        return await message.reply_text("⚠️ لا يوجد بوتات مصنوعة بعد")
    
    stats_text = "📊 إحصائيات البوتات المصنوعة:\n\n"
    total_users = 0
    total_groups = 0
    
    for bot_data in bots_list:
        bot_username = bot_data["username"]
        dev_id = bot_data["dev"]
        
        try:
            # إنشاء عميل للبوت
            bot_client = Client(
                f"stats_{bot_username}",
                api_id=API_ID,
                api_hash=API_HASH,
                bot_token=None,
                in_memory=True
            )
            
            try:
                with open(f"Files/{bot_username}/.env", "r") as env_file:
                    env_vars = env_file.read()
                    bot_token = None
                    for line in env_vars.split("\n"):
                        if line.startswith("BOT_TOKEN"):
                            bot_token = line.split("=")[1].strip()
                            break
                    
                    if not bot_token:
                        raise Exception("لم يتم العثور على التوكن")
                    
                    bot_client.bot_token = bot_token
                  
                    await bot_client.start()
                    
                    bot_me = await bot_client.get_me()
                    bot_chats = await bot_client.get_dialogs()
                    
                    groups = 0
                    users = 0
                    
                    for chat in bot_chats:
                        if chat.chat.type == "private":
                            users += 1
                        elif chat.chat.type in ["group", "supergroup"]:
                            groups += 1
                    
                    total_users += users
                    total_groups += groups
                    
                    stats_text += (
                        f"🤖 البوت: @{bot_username}\n"
                        f"👤 المطور: <code>{dev_id}</code>\n"
                        f"👥 المستخدمين: {users}\n"
                        f"👥 المجموعات: {groups}\n"
                        f"────────────────────\n"
                    )
                    
                    await bot_client.stop()
                    
            except Exception as e:
                stats_text += (
                    f"🤖 البوت: @{bot_username}\n"
                    f"👤 المطور: <code>{dev_id}</code>\n"
                    f"❌ فشل في جلب الإحصائيات: {str(e)}\n"
                    f"────────────────────\n"
                )
                continue
                
        except Exception as e:
            stats_text += (
                f"🤖 البوت: @{bot_username}\n"
                f"👤 المطور: <code>{dev_id}</code>\n"
                f"❌ فشل في الاتصال بالبوت: {str(e)}\n"
                f"────────────────────\n"
            )
            continue
    
    # إضافة الإجمالي
    stats_text += (
        f"\n📈 الإجمالي:\n"
        f"👥 إجمالي المستخدمين: {total_users}\n"
        f"👥 إجمالي المجموعات: {total_groups}\n"
        f"🤖 عدد البوتات: {len(bots_list)}\n"
    )
    
    await message.reply_text(stats_text, disable_web_page_preview=True)