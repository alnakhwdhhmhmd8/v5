from pyrogram import Client, filters
import requests
import re
from VeRoNMusic import app

# إعدادات API
COINMARKETCAP_API_KEY = '57ed7825-b098-4cfb-894c-674e7c070ec8'
EXCHANGERATE_API_KEY = '9cc674720b52085745c95ec7'  # احصل على مفتاح من https://www.exchangerate-api.com/

# روابط API
TON_PRICE_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=TON"
EXCHANGE_RATE_URL = f"https://v6.exchangerate-api.com/v6/{EXCHANGERATE_API_KEY}/latest/USD"

# هيدرات لطلب API
coinmarketcap_headers = {
    'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY,
    'Accept': 'application/json'
}

def get_ton_prices():
    try:
        # الحصول على سعر TON بالدولار
        ton_response = requests.get(TON_PRICE_URL, headers=coinmarketcap_headers)
        ton_data = ton_response.json()
        
        if ton_response.status_code != 200:
            return None, "فشل في جلب بيانات التون"
            
        usd_price = ton_data['data']['TON']['quote']['USD']['price']
        
        # الحصول على أسعار الصرف
        exchange_response = requests.get(EXCHANGE_RATE_URL)
        exchange_data = exchange_response.json()
        
        if exchange_response.status_code != 200 or exchange_data['result'] != 'success':
            return None, "فشل في جلب أسعار الصرف"
            
        egp_rate = exchange_data['conversion_rates']['EGP']
        iqd_rate = exchange_data['conversion_rates']['IQD']
        
        # حساب الأسعار المحولة
        egp_price = usd_price * egp_rate
        iqd_price = usd_price * iqd_rate
        
        return {
            'usd': usd_price,
            'egp': egp_price,
            'iqd': iqd_price
        }, None
        
    except Exception as e:
        return None, f"حدث خطأ: {str(e)}"

@app.on_message(filters.command(["تون"], ""), group=838838283)
async def send_prices(client, message):
    prices, error = get_ton_prices()
    
    if error:
        await message.reply_text(f"⚠️ {error}")
        return
    
    response_msg = (
        "💰 **أسعار TON الحالية:**\n\n"
        f"• 🇺🇸 دولار أمريكي: ${prices['usd']:.2f}\n"
        f"• 🇪🇬 جنيه مصري: ج.م {prices['egp']:.2f}\n"
        f"• 🇮🇶 دينار عراقي: د.ع {prices['iqd']:.2f}"
    )
    
    await message.reply_text(response_msg)