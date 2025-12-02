from bs4 import BeautifulSoup
import requests

def simple_search():
    url = ('https://time-in.ru/time/vladikavkaz?ysclid=miexcp4t9s791336017')

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    all_text = soup.get_text()

    mydivs = soup.find_all("div", {"class": "time-city-time-value"})
    #print(mydivs.get_text())
    for el in soup.find_all('div', attrs={'class': 'time-city-time-value'}):
        parsed_time = el.get_text()
        return parsed_time
"""
    if "" in all_text.lower():
        print("Слово есть на странице")
        lines = all_text.split("\n")

        for line in lines:
            if "" in line.lower():
                print(f" {line.strip()}")
    else:
                print("Слово не упоминается на странице")
"""
#simple_search()