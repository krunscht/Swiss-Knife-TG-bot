import telebot
import configparser

config = configparser.ConfigParser()
config.read("bot_config.ini")

BOT_TOKEN = config["telegram"]["BOT_TOKEN"]
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("/start")
    user_name = message.from_user.first_name
    bot.send_message(
        message.chat.id,
        f"Здравствуйте, {user_name}!",
        reply_markup=keyboard)
    