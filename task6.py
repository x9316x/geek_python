'''
Задача 6: Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.
Пример:
385916 -> yes
123456 -> no
'''
ticket_num = int(input('Введите номер билета: '))

first_half = ticket_num // 1000
second_half = ticket_num % 1000

first_half_sum = first_half // 100 + first_half // 10 % 10 + first_half % 10
second_half_sum = second_half // 100 + second_half // 10 % 10 + second_half % 10

if first_half_sum == second_half_sum:
    print('Билет счастливый, поздравляем!')
else:
    print('Билет не является счастливым, попробуй ещё раз!')