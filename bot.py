import telebot
import random
from parser import simple_search
import configparser

config = configparser.ConfigParser()
config.read("bot_config.ini")
BOT_TOKEN = config["telegram"]["BOT_TOKEN"]
bot = telebot.TeleBot(BOT_TOKEN)

# старт
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # кнопка старт создатьь
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("/start")
    
    #распознавание юза
    user_name = message.from_user.first_name
    
    bot.send_message(
        message.chat.id,
        f"Здравствуйте, {user_name}!",
        reply_markup=keyboard
    )

@bot.message_handler(commands=['random'])
def send_random(message):
    
    monet = random.choice(["орел", "решка"])
    # отправка числа
    bot.send_message(message.chat.id, f"Я бросил монету и выпал(-a) {monet}")

@bot.message_handler(commands=['startparser'])
def send_parser(message):
    start_parser = simple_search()
    bot.send_message(message.chat.id, f"Результат работы парсера: {start_parser}")
bot.polling()