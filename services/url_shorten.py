import configparser
import telebot
import pyshorteners

config = configparser.ConfigParser()
config.read("bot_config.ini")

BOT_TOKEN = config["telegram"]["BOT_TOKEN"]
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['shorten'])
def shorten_link(message):
    try:

        long_url = message.text.split(' ', 1)[1]
    except IndexError:
        
        bot.reply_to(message, "Пожалуйста, прикрепите ссылку. Пример: /shorten https://example.com")

        return

    try:

        s = pyshorteners.Shortener()
        short_link = s.isgd.short(long_url)
        bot.reply_to(message, f"Готово: {short_link}")

    except Exception as e:
        bot.reply_to(message, f"Не удалось сократить ссылку. Ошибка: {e}")