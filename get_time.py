import configparser
import pytz
from datetime import datetime
import telebot
from until.until import get_time

config = configparser.ConfigParser()
config.read("bot_config.ini")

BOT_TOKEN = config["telegram"]["BOT_TOKEN"]
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['get_time'])
def send_time(message):
    bot.send_message(message.chat.id, f"Текущее время по МСК: {get_time()}")