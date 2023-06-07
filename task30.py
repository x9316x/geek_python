'''
Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести 
с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
'''

first_element = int(input('Введите первый элемент арифмитической прогрессии: '))
difference = int(input('Введите значение разности d: '))
arithmetic_progression_count = int(input('Введите количество элементов прогрессии: '))

arithmetic_progression = [first_element + i * difference for i in range(arithmetic_progression_count)]

print(*arithmetic_progression)