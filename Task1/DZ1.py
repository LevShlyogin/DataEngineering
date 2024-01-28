import re
from collections import Counter

#Считываем файл
filename = 'C:/Users/User/OneDrive/Рабочий стол/text_1_var_54.txt'
with open(filename) as file:
    text = file.read()

    # Удаляем знаки препинания
    text = re.sub(r'[.,"\'-?:!;]', ' ', text)

    # Устраняем множественные пробелы и приводим все буквы к нижнему регистру
    text = re.sub(r'\s+', ' ', text).lower()

    # Разбиваем текст на слова
    words = text.split()

    # Подсчитываем частоту каждого слова
    word_frequency = Counter(words)

    # Сортируем слова по убыванию частоты
    sorted_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

    # Открываем файл для записи результатов
    with open('output1.txt', 'w') as output_file:

    # Записываем результаты в файл
        for word, frequency in sorted_words:
            output_file.write(f'{word}: {frequency}\n')
