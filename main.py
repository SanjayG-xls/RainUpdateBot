import o

import requests
import datetime
import pytz

API_KEY = os.environ['OWM_API_KEY']
CITY = os.environ['LAT_LONG']
BOT_TOKEN = os.environ['XLSXRAIN_BOT_TOKEN']
CHAT_ID = os.environ['XLSXRAIN_CHAT_ID']
IST = pytz.timezone('Asia/Kolkata')

def get_weather_forecast():
    try:
        url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={CITY}&days=2"
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            return f"❌ API Error: {data['error']['message']}"

        forecast = data["forecast"]["forecastday"][1]  # Tomorrow's forecast
        rain_chance = int(forecast["day"]["daily_chance_of_rain"])

        if rain_chance > 50:
            return f"🌧️☔ Heads up, Kundrathur! There's a 🌊 **{rain_chance}%** chance of rain tomorrow — pack your umbrella and maybe a boat? 🛶💦"
        elif rain_chance > 20:
            return f"🌦️ Hmmm... Sky’s feeling moody 🌫️ — **{rain_chance}%** chance of rain in Kundrathur tomorrow! Keep a hoodie handy just in case 🎒☁️"
        else:
            return f"☀️🌈 Kundrathur's got sunshine vibes tomorrow! Only **{rain_chance}%** chance of rain — soak up the sun, not the storm 😎🌼"

    except Exception as e:
        return f"⚠️ Error fetching forecast: {str(e)}"

def send_telegram_message(message):
    telegram_url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(telegram_url, data=payload)

def main():
    message = get_weather_forecast()
    send_telegram_message(message)
    print("Weather message sent.")

if __name__ == '__main__':
    main()
