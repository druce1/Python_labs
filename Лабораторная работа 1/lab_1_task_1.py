numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Индекс пропущенного значения
missing_index = 4

# Сумма всех значений
sum_numbers = sum(numbers[:missing_index]) + sum(numbers[missing_index+1:])

# Среднее арифметическое
average = sum_numbers / len(numbers)

# Замена пропущенного элемента
numbers[missing_index] = average

print("Измененный список:", numbers)
