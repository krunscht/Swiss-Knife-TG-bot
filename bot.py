import telebot
import configparser
from random_side import send_random
from get_time import send_time
from url_shorten import shorten_link
from passgen import password_generate

config = configparser.ConfigParser()
config.read("bot_config.ini")
BOT_TOKEN = config["telegram"]["BOT_TOKEN"]
bot = telebot.TeleBot(BOT_TOKEN)
CUTTLY_API_KEY = config["cuttly"]["API_KEY"]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("/start")
    user_name = message.from_user.first_name
    bot.send_message(
        message.chat.id,
        f"Здравствуйте, {user_name}!",
        reply_markup=keyboard)

@bot.message_handler(commands=['random'])
def call_random_side(message):
    send_random(message)

@bot.message_handler(commands=['get_time'])
def call_get_time(message):
    send_time(message)

@bot.message_handler(commands=['shorten'])
def call_shorten(message):
    shorten_link(message)

@bot.message_handler(commands=['gen_pass'])
def call_passgen(message):
    password_generate(message, bot)

print("Бот запущен...")
bot.infinity_polling(timeout=10)