import configparser
import pytz
from datetime import datetime
import telebot

config = configparser.ConfigParser()
config.read("bot_config.ini")

BOT_TOKEN = config["telegram"]["BOT_TOKEN"]
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['get_time'])
def send_time(message):
    #чтоб чекать time
    tz_time = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(tz_time)
    formatted_time = current_time.strftime('%H:%M:%S')
    bot.send_message(message.chat.id, f"Текущее время по МСК: {formatted_time}")