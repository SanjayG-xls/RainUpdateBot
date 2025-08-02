import requests
import datetime
import pytz
import os

API_KEY = os.environ['OWM_API_KEY']
LAT = 12.9676  # Kundrathur
LON = 80.0851
BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']
IST = pytz.timezone('Asia/Kolkata')

def get_weather_forecast():
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&exclude=current,minutely,hourly,alerts&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()

    tomorrow = data['daily'][1]
    rain_prob = tomorrow.get('pop', 0) * 100

    if rain_prob > 50:
        message = f"🌧️ Rain is likely tomorrow with a {rain_prob:.0f}% chance."
    elif rain_prob > 20:
        message = f"🌦️ There's a {rain_prob:.0f}% chance of rain tomorrow. Stay alert."
    else:
        message = f"☀️ No rain expected tomorrow. Chance is only {rain_prob:.0f}%."

    return message

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
