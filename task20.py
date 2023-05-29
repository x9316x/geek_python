'''
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
*Пример:*
ноутбук
    12
'''
word = input('Введите слово: ')
word = word.upper()
points = 0

ru_alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

point_1_en = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']
point_2_en = ['D', 'G']
point_3_en = ['B', 'C', 'M', 'P']
point_4_en = ['F', 'H', 'V', 'W', 'Y']
point_5_en = ['K']
point_8_en = ['J', 'X']
point_10_en = ['Q', 'Z']

point_1_ru = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
point_2_ru = ['Д', 'К', 'Л', 'М', 'П', 'У']
point_3_ru = ['Б', 'Г', 'Ё', 'Ь', 'Я']
point_4_ru = ['Й', 'Ы']
point_5_ru = ['Ж', 'З', 'Х', 'Ц', 'Ч']
point_8_ru = ['Ш', 'Э', 'Ю']
point_10_ru = ['Ф', 'Щ', 'Ъ']

if word[0] in ru_alphabet:
	for i in range(len(word)):
		if word[i] in point_1_ru:
			points += 1
		elif word[i] in point_2_ru:
			points += 2
		elif word[i] in point_3_ru:
			points += 3
		elif word[i] in point_4_ru:
			points += 4
		elif word[i] in point_5_ru:
			points += 5
		elif word[i] in point_8_ru:
			points += 8
		elif word[i] in point_10_ru:
			points += 10
else:
	for i in range(len(word)):
		if word[i] in point_1_en:
			points += 1
		elif word[i] in point_2_en:
			points += 2
		elif word[i] in point_3_en:
			points += 3
		elif word[i] in point_4_en:
			points += 4
		elif word[i] in point_5_en:
			points += 5
		elif word[i] in point_8_en:
			points += 8
		elif word[i] in point_10_en:
			points += 10
			
print(f'Вы набрали {points} очков(-а)')
