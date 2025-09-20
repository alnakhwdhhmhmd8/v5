from pyrogram import Client, filters
from pyrogram.types import Message
import random
from VeRoNMusic import app

def calculate_gay_percentage():
    return random.randint(1, 100)

def generate_gay_response(gay_percentage):
    if gay_percentage < 30:
        return "- انت رجـل كالسهم \n\n√"
    elif 30 <= gay_percentage < 70:
        return "- عندك نسبه محن مش كتير \n\n√"
    else:
        return "- انت ممحون اكتر من الست الحامل \n\n√"

@app.on_message(filters.command(["نسبة الرجوله"], ""), group=6752456442)
async def gay_calculator_command(client, message: Message):
    gay_percentage = calculate_gay_percentage()
    gay_response = generate_gay_response(gay_percentage)
    await message.reply_text(f"↢ نسبة الرجوله: {gay_percentage}%\n{gay_response}")