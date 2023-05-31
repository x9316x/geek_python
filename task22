'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.
'''
n = int(input('Введите количество элементов массива № 1 - n: '))
m = int(input('Введите количество элементов массива № 2 - m: '))

arr_n = [0] * n
arr_m = [0] * m
res_arr = []

for i in range(n):
    arr_n[i] = int(input(f'Введите элемент массива № 1 под номером {i}: '))

for j in range(m):
    arr_m[j] = int(input(f'Введите элемент массива № 2 под номером {j}: '))

print('Массив № 1:', *arr_n)
print('Массив № 2:', *arr_m)

if n < m:
    for i in range(n):
        if arr_n[i] in arr_m:
            if not arr_n[i] in res_arr:
                res_arr.append(arr_n[i])
else:
    for j in range(m):
        if arr_m[j] in arr_n:
            if not arr_m[j] in res_arr:
                res_arr.append(arr_m[j])

sorted(res_arr)

print(f'Ответ: ', *res_arr)
