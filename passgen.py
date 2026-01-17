from random import choice
import telebot
import configparser

config = configparser.ConfigParser()
config.read("bot_config.ini")

BOT_TOKEN = config["telegram"]["BOT_TOKEN"]
bot = telebot.TeleBot(BOT_TOKEN)

def generate_password():
    number = "1234567890"
    letter = 'qwertyuiopasdfghjklzxcvbnm'
    big_letter = letter.upper()
    symbol = '`~!@#$%^&*()№;%:?-_=+<>/'
    total = number + letter + big_letter + symbol
    password = ''

    for i in range(8):
        password += choice(total)
    return password

@bot.message_handler(commands=['gen_pass'])
def password_generate(message, bot):
    password = generate_password()
    bot.send_message(message.chat.id, f'Пароль: {password}')
