import os
import telebot
from Levenshtein import distance

TOKEN = "7399695363:AAEdEeMVsw8ST1MHanOGLb8gJ6UxpfS-5mY"
GRUP_NAME = "Zappelin Crypto Pro"
LOG_CHANNEL = "@zappelin_logs"
WHITELIST_USERS = [kara]
STRICT_MODE = True


KATA_KASAR_GLOBAL = {
    "id": ["anjing", "babi", "bangsat", "kontol", "jancok"],
    "en": ["fuck", "shit", "bitch", "asshole"],
    "ar": ["كلب", "عاهر"],
    "es": ["puta", "cabrón"],
    "ru": ["сука", "блядь"]
}

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def handle_message(message):
    if message.from_user.id in WHITELIST_USERS:
        return
    
    text_lower = message.text.lower()
    
    
    for lang, words in KATA_KASAR_GLOBAL.items():
        if any(distance(word, text_lower) <= 2 for word in words):
            bot.delete_message(message.chat.id, message.message_id)
            if STRICT_MODE:
                bot.ban_chat_member(message.chat.id, message.from_user.id)
            break

@bot.message_handler(commands=["chart"])
def send_chart(message):
    try:
        symbol = message.text.split()[1].upper()
        bot.send_photo(
            message.chat.id, 
            f"https://www.tradingview.com/x/{symbol}/",
            caption=f"📊 {symbol} | {GRUP_NAME}"
        )
    except:
        bot.reply_to(message, "Gunakan: /chart BTCUSD")

print("🤖 Bot aktif!")
bot.polling()

