import requests
import json

# API ключ OpenWeatherMap
api_key = "cbb3ae4c5109c8eb9e8052804d41eb36"

# Запрашиваем данные о текущей погоде с использованием API ключа
response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q=Moscow,ru&appid={api_key}")
data = json.loads(response.text)

# Преобразование JSON в HTML представление
html = f"<h1>Погода в городе {data['name']}</h1>"
html += f"<p>Температура: {data['main']['temp']} градусов Цельсия</p>"
html += f"<p>Ощущается как: {data['main']['feels_like']} градусов Цельсия</p>"
html += f"<p>Скорость ветра: {data['wind']['speed']} м/с</p>"

# Запись вывода в HTML файл
with open("weather.html", "w", encoding='utf-8', newline="") as file:
    file.write(html)
