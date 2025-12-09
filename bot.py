#ымпорты
import telebot
import random
import configparser
import pytz
from datetime import datetime
import requests

#чтоб бота не украли
config = configparser.ConfigParser()
config.read("bot_config.ini")
BOT_TOKEN = config["telegram"]["BOT_TOKEN"]
bot = telebot.TeleBot(BOT_TOKEN)
#апи сократитъ ссылку
CUTTLY_API_KEY = config["cuttly"]["API_KEY"]

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
#orel or reshka
@bot.message_handler(commands=['random'])
def send_random(message):
    
    monet = random.choice(["орел", "решка"])
    # result
    bot.send_message(message.chat.id, f"Я бросил монету и выпал(-a) {monet}")

@bot.message_handler(commands=['get_time'])
def send_time(message):
    #чтоб чекать time
    tz_vladikavkaz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(tz_vladikavkaz)
    formatted_time = current_time.strftime('%H:%M:%S')
    bot.send_message(message.chat.id, f"Текущее время по МСК: {formatted_time}")

#сокращалка ссылок
@bot.message_handler(commands=['shorten'])
def shorten_link(message):
    try:
        long_url = message.text.split(' ', 1)[1]
        #если юзер скинул херню а не ссылку
    except IndexError:
        bot.reply_to(message, "Пожалуйста, прикрепите ссылку. Usage: `/shorten https://example.com`")
        return

    api_url = f"https://cutt.ly/api/api.php?key={CUTTLY_API_KEY}&short={long_url}"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        bot.reply_to(message, f"Ошибка при запросе к Cuttly: {e}")
        return

    data = response.json()
    #это кроч если выполнилось или не выполнилось
    if data['url']['status'] == 7:
        short_link = data['url']['shortLink']
        bot.reply_to(message, f"Готово: {short_link}")
    else:
        error_message = data['url']['title']
        bot.reply_to(message, f"Не удалось сократить ссылку.", "\n", 'Ошибка Cuttly: {error_message}')
bot.infinity_polling()