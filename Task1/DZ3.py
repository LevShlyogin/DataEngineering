import math

# Считываем файл
filename = 'C:/Users/User/OneDrive/Рабочий стол/text_3_var_54'
output_filename = 'output3.txt'
with open(filename) as file:
    lines = file.readlines()

result_lines = []

# Обработка строк
for line in lines:
    nums = line.split(",")

    # Замена пропусков "NA" на среднее значение соседних чисел
    for i in range(len(nums)):
        if nums[i] == "NA":
            # Проверяем соседнее число слева
            left = nums[i - 1] if i > 0 else "NA"

            # Проверяем соседнее число справа
            right = nums[i + 1] if i < len(nums) - 1 else "NA"

            # Вычисляем среднее значение соседних чисел
            if left != "NA" and right != "NA":
                avg = (float(left) + float(right)) / 2
                nums[i] = str(avg)
            elif left != "NA":
                nums[i] = left
            elif right != "NA":
                nums[i] = right

    # Фильтрация значений: исключение чисел, корень квадратный из которых будет меньше 104
    filtered_nums = [num for num in nums if math.sqrt(float(num)) >= 104]

    # Запись отфильтрованных чисел в строку
    filtered_line = ' '.join(filtered_nums)
    result_lines.append(filtered_line)

# Запись результатов в файл
with open(output_filename, 'w') as output_file:
    output_file.write('\n'.join(result_lines))
