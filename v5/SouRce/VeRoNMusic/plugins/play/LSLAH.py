from requests import Session
from requests import Response
from typing import Union
from VeRoNMusic import app
from pyrogram import Client, filters
from pyrogram.types import Message



s = Session()
@app.on_message(filters.regex(r"^(مواقيت صلاة|مواقيت صلاه|وقت الصلاه)"), group=800906)
async def sendAdhan(_: Client, message: Message) -> None:
    address: str = message.text.rsplit(maxsplit=1)[-1]
    if address == "مواقيت الصلاة": return await message.reply(" اكتب اسم المنطقه بجانب الأمر،")
    adhan: Union[str, bool] = getAdhan(address)
    if not adhan: return await message.reply(" حدث خطأ أثناء جلب مواقيت الصلاة.", reply_to_message_id=message.id)
    await message.reply(adhan, reply_to_message_id=message.id)    


def getAdhan(address: str) -> Union[str, bool]:
    method: int = 1
    params = {
        "address" : address,
        "method" : method, 
        "school" : 0
    }
    res: Response = s.get("http://api.aladhan.com/timingsByAddress", params=params)
    data: dict = res.json()
    if data["code"] != 200: return print(data)
    data: dict = data["data"]
    timings: dict = data["timings"]
    date: dict = data["date"]["hijri"]
    weekday: str = date["weekday"]["ar"] + " - " + date["weekday"]["en"]
    month: str = date["month"]["ar"] + " - " + date["month"]["en"]
    date: str = date["date"]
    caption: str = f"<b>[سوࢪس فيࢪوטּ | 𝙎𝙤𝙪𝙧𝙘𝙚 𝙑𝙚𝙧𝙤𝙣. #]</b>\n<u>اوقات الصلاه من فيجا</u>\n╮❖ الـفـجـر: {timings['Fajr']}\n│᚜❖ الـشـروق: {timings['Sunrise']}\n│᚜❖ الـظـهـر: {timings['Dhuhr']}\n│᚜❖ الـعـصـر: {timings['Asr']}\n│᚜❖ الـمـغـرب: {timings['Maghrib']}\n╯❖ الـعـشـاء: {timings['Isha']}\n╮❖  اللمساك : {timings['Imsak']}\n│᚜❖ الثلت الاول من الليل: {timings['Firstthird']}\n│᚜❖ منتصف الليل: {timings['Midnight']}\n╯❖ الثلث الاخير من الليل: {timings['Lastthird']}"
    caption += f"\n\n╮❖ التاريخ: {date} (هـ)\n│᚜❖ يـوم: {weekday}\n╯❖ الشهر: {month}"
    return caption