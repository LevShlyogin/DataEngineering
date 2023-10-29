# Импортируем библиотеку
import pandas as pd

# Считываем файл
df = pd.read_csv('C:/Users/User/OneDrive/Рабочий стол/text_4_var_54.csv')
split_data = df.copy()

# Добавляем заголовки столбцов
split_data.columns =['Порядковый номер', 'Имя', 'Фамилия', 'Возраст', 'Зарплата', 'Номер телефона']

# Удаляем столбец с номером телефона
split_data.drop('Номер телефона', axis=1, inplace=True)

# Преобразуем столбец
zp = split_data['Зарплата'].map(lambda x: x.rstrip('₽')).astype(int)

# Заменяем столбец
split_data['Зарплата'] = zp

# Находим среднюю зарплат
av_sal = zp.mean()

# Фильтруем по средней зарплате
select_data_zp = split_data[split_data['Зарплата'] >= av_sal]

# Фильтруем по возрасту
select_data_age = select_data_zp[select_data_zp['Возраст'] >= (25 + 54 % 10)]

# Сортируем по порядковому номеру
sort_data = select_data_age.sort_values(by=['Порядковый номер'])

# Преобразуем таблицу
sort_data['ФИО'] = sort_data['Имя'] + " " + sort_data['Фамилия']
sort_data.drop('Имя', axis=1, inplace=True)
sort_data.drop('Фамилия', axis=1, inplace=True)

sort_data.to_csv('output4.csv')