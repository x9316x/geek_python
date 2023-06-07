'''
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''
index_array = []

array_length = int(input('Введите длину массива: '))
array = [int(input("Введите элемент №" + str(i+1) + ": ")) for i in range(array_length)]

print(*array)

segment_start = int(input('Введите начало диапазона: '))
segment_end = int(input('Введите конец диапазона: '))

for i in range(array_length):
    if array[i] <= segment_end and array[i] >= segment_start:
        index_array.append(i)

print(*index_array)