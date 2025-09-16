import telebot

# Bu yerga Telegram bot tokeningizni yozing
TOKEN = "7734429679:AAH0gaP4WbkyjHpwnjMJXNTpmxW3uKMoHbQ"
bot = telebot.TeleBot(TOKEN)

# /start buyrug'iga javob
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Salom! Bot ishlayapti ✅")

# /products buyrug'iga javob
@bot.message_handler(commands=['products'])
def show_products(message):
    products_list = [
        {"name": "Kofta", "price": "50 000", "color": "qora", "size": "M"},
        {"name": "Sport kiyim", "price": "120 000", "color": "yashil", "size": "L"},
        {"name": "Oyoq kiyim", "price": "200 000", "color": "qizil", "size": "42"}
    ]
    
    response = "Bizning mahsulotlar:\n\n"
    for p in products_list:
        response += f"{p['name']} — {p['price']} so'm, rangi: {p['color']}, o'lchami: {p['size']}\n"
    
    bot.send_message(message.chat.id, response)

# Botni ishga tushirish
print("Bot ishga tushdi...")
bot.polling(none_stop=True)

import telebot

# Bu yerga o'zingizning bot tokeningizni yozasiz
TOKEN = "7734429679:AAH0gaP4WbkyjHpwnjMJXNTpmxW3uKMoHbQ"
bot = telebot.TeleBot(TOKEN)

# /start buyrug'ini qabul qiladi
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom! Bot ishlayapti ✅")

# /products buyrug'i uchun
@bot.message_handler(commands=['products'])
def products(message):
    # Mana bu yerda o'z mahsulotlaringni qo'yasan
    items = [
        "1. Futbolka - Narxi: 50,000 so'm - Rang: Oq - Razmer: M",
        "2. Shapka - Narxi: 30,000 so'm - Rang: Qora - Razmer: Free size",
        "3. Krossovka - Narxi: 200,000 so'm - Rang: Oq/Qora - Razmer: 42"
    ]
    bot.send_message(message.chat.id, "\n".join(items))

# Botni ishga tushuramiz

bot.polling()
from flask import Flask
import threading, os

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running!"

def run_bot():
    bot.polling(none_stop=True)

threading.Thread(target=run_bot).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
