"""
Задача:
Почесть с помощью pandas файл california_housing_test.csv
Посмотрреть сколько в нем строк и столбцов,
определить какой тип данных имеют столбцы
"""
from pandas import read_csv
data = read_csv('california_housing_test.csv')
print(data.shape) #Почесть с помощью pandas файл california_housing_test.csv Посмотрреть сколько в нем строк и столбцов,
print(data)
print(data.dtypes) #определить какой тип данных имеют столбцы
print(data.info()) #инфа по таблице
print(data.describe()) # 

