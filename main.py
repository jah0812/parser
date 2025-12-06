import requests
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd

# Список для хранения данных о книгах
travel_books = []

# Получаем URL страницы
url = "https://books.toscrape.com"
response = requests.get(url)

# Получаем HTML код страницы
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")


# Проверка статуса ответа
if response.status_code == 200:
    print("Успешно получили страницу!")
else:
    f'Ошибка: {response.status_code}'
    

# Поиск заголовка страницы
title = soup.title.text
print(f'Заголовок страницы: {title}')

# Поиск всех карточек книг
books = soup.find_all("article", class_="product_pod" )
print(books)

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.p["class"][-1]

    travel_books.append({
        "Title": title,
        "Price": price,
        "Rating": rating,
    })

# Создаем датафрейм из списка словарей
df = pd.DataFrame(travel_books)

# Сохраняем датафрейм в CSV файл
df.to_csv("travel_books.csv", index=False)

print("Данные успешно сохранены в файл travel_books.csv!")
