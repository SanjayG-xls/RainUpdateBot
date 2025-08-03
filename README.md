# 🌧️ Telegram Rain Forecast Bot

A Python script that fetches tomorrow’s rain forecast using [WeatherAPI](https://www.weatherapi.com/) and sends an alert to a Telegram chat via a bot.

💖 Support This Project
If you found this project useful or want to support its development, consider contributing:

👉 [![Support via Linktree](https://img.shields.io/badge/Support-Linktree-blueviolet?logo=buymeacoffee&style=flat-square)](https://linktr.ee/Sanjay_xlsX)

Every little bit helps! 🙌

## 📦 Features

- ☁️ Gets **tomorrow’s** rain forecast based on your city (latitude & longitude).
- 🤖 Sends formatted alerts to a **Telegram bot chat**.
- 🌦️ Custom message formatting based on chance of rain.
- 🕒 Designed for daily scheduled use (e.g., via GitHub Actions or cron).

---

## 🚀 How It Works

1. Fetches weather forecast using `WeatherAPI`.
2. Extracts the chance of rain for **tomorrow**.
3. Crafts a friendly, emoji-based message.
4. Sends it to your Telegram chat using the Telegram Bot API.

---

## 🔧 Environment Variables

Before running the script, set the following environment variables:

| Variable Name          | Description                                 |
|------------------------|---------------------------------------------|
| `OWM_API_KEY`          | Your [weatherapi.com](https://weatherapi.com) API key |
| `LAT_LONG`             | Location in `"latitude,longitude"` format (e.g. `xxxxx,xxxxx`) |
| `XLSXRAIN_BOT_TOKEN`   | Your Telegram bot token (from [@BotFather](https://t.me/BotFather)) |
| `XLSXRAIN_CHAT_ID`     | Chat ID where messages will be sent         |

---

### 📬 Example Output

🌦️ Hmmm... Sky’s feeling moody 🌫️ — **35%** chance of rain in **IN YOUR AREA** tomorrow!  
Keep a hoodie handy just in case 🎒☁️

---

### 📌 Author

**Sanjay XLSX**  
🔗 [Linktree](https://linktr.ee/Sanjay_xlsX)


