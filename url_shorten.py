import configparser
import telebot
import requests

config = configparser.ConfigParser()
config.read("bot_config.ini")

BOT_TOKEN = config["telegram"]["BOT_TOKEN"]
bot = telebot.TeleBot(BOT_TOKEN)

CUTTLY_API_KEY = config["cuttly"]["API_KEY"]

@bot.message_handler(commands=['shorten'])
def shorten_link(message):
    try:
        long_url = message.text.split(' ', 1)[1]

    except IndexError:
        bot.reply_to(message, "Пожалуйста, прикрепите ссылку. Пример: /shorten https://example.com")
        return

    api_url = f"https://cutt.ly/api/api.php?key={CUTTLY_API_KEY}&short={long_url}"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        bot.reply_to(message, f"Ошибка при запросе к Cuttly: {e}")
        return

    data = response.json()
    
    if data['url']['status'] == 7:
        short_link = data['url']['shortLink']
        bot.reply_to(message, f"Готово: {short_link}")
    else:
        error_message = data['url']['title']
        bot.reply_to(message, f"Не удалось сократить ссылку.", "\n", 'Ошибка Cuttly: {error_message}')