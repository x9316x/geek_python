'''
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
'''
import random

n = int(input('Введите число монет n: '))

coin = ['eagle', 'tails']
coin_tosses = []
eagle = 0
tails = 0

for i in range(n):
	coin_tosses.append(random.choice(coin))
	print(coin_tosses[i])
	
for i in range(n):
		if coin_tosses[i] == 'eagle':
			eagle += 1
		else:
			tails += 1

if eagle > tails:
	print(f'Минимальное количество монет, которые нужно перевернуть - {tails}')
elif eagle == tails:
	print(f'Минимальное количество монет, которые нужно перевернуть - {tails}')
else:
	print(f'Минимальное количество монет, которые нужно перевернуть - {eagle}')
