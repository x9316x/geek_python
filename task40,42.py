'''
Задача 40: Работать с файлом california_housing_train.csv, который находится
в папке sample_data. Определить среднюю стоимость дома, где кол-во людей
от 0 до 500 (population).

Задача 42: Узнать какая максимальная households в зоне минимального
значения population.
'''

import pandas as pd
import os

directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(directory, "sample_data", "california_housing_train.csv")

df = pd.read_csv(file_path)

# Задача 40:
filtered_df = df[(df['population'] > 0) & (df['population'] <= 500)] 

mean_value = filtered_df['median_house_value'].mean()

print(f'Средняя стоимость дома, где количество людей от 0 до 500: {mean_value}')

# Задача 42: 
min_population = df['population'].min() 

filtered_df = df[df['population'] == min_population] 

max_households = filtered_df['households'].max()

print(f'Максимальное значение households в зоне минимального значения population: {max_households}')
