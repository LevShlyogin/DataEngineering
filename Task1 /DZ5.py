# Импорт библиотек
import csv
from bs4 import BeautifulSoup

# Создание пустого списка
items = list()

# Чтение HTML из файла
with open("C:/Users/User/OneDrive/Рабочий стол/text_5_var_54.html", "r", encoding='utf-8') as file:
    lines = file.readlines()
    html = ''
    for line in lines:
        html += line

    # Создание объекта BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Нахождение всех строк таблицы
    rows = soup.find_all("tr")
    rows = rows[1:]
    for row in rows:
        cells = row.find_all("td")
        item = {
            'company': cells[0].text,
            'contact': cells[1].text,
            'country': cells[2].text,
            'price': cells[3].text,
            'item': cells[3].text
        }
        items.append(item)

# Открытие CSV файла для записи
with open("output5.csv", "w", encoding='utf-8', newline="") as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for item in items:
        writer.writerow(item.values())
