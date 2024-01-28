# Считываем файл
filename = 'C:/Users/User/OneDrive/Рабочий стол/text_2_var_54'
with open(filename) as file:
    lines = file.readlines()
sum_list = list()

# Считываем строки и суммируем числа
for line in lines:
    nums = line.split(':')
    sum_nums = 0
    for num in nums:
        sum_nums += int(num)
    sum_list.append(sum_nums)

# Открываем файл для записи результатов
with open('output2.txt', 'w') as output_file:

    # Записываем результаты в файл
    for val in sum_list:
        output_file.write(str(val) + '\n')
