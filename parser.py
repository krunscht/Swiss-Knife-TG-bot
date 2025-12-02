# parser.py
from bs4 import BeautifulSoup
import requests

def simple_search():
    url = 'https://time-in.ru/time/vladikavkaz'

    # Создаем заголовок, чтобы притвориться браузером
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    try:
        # Передаем заголовки в наш запрос
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка, что запрос прошел успешно (код 200)

        soup = BeautifulSoup(response.text, "html.parser")

        # Ищем нужный элемент. find_all вернет список, но нам нужен первый элемент.
        # Поэтому можно использовать find() - он вернет первый найденный элемент.
        time_element = soup.find("div", {"class": "time-city-time-value"})
        
        if time_element:
            parsed_time = time_element.get_text(strip=True) # strip=True уберет лишние пробелы
            return parsed_time
        else:
            return "Не удалось найти время на странице."

    except requests.exceptions.RequestException as e:
        # Если любая ошибка сети (прокси, таймаут, нет сайта и т.д.)
        return f"Ошибка при запросе к сайту: {e}"
