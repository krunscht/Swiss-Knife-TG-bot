import telebot
import configparser
from until.until import check_monet

config = configparser.ConfigParser()
config.read("bot_config.ini")

BOT_TOKEN = config["telegram"]["BOT_TOKEN"]
bot = telebot.TeleBot(BOT_TOKEN)

#orel or reshka
@bot.message_handler(commands=['random'])
def send_random(message):
    bot.send_message(message.chat.id, f"Я бросил монету и выпал(-a) {check_monet()}")