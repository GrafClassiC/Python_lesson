"""
Задача:
Почесть с помощью pandas файл california_housing_test.csv
Посмотрреть сколько в нем строк и столбцов,
определить какой тип данных имеют столбцы
"""
# from pandas import read_csv
# data = read_csv('california_housing_test.csv') #Почесть с помощью pandas файл california_housing_test.csv Посмотрреть сколько в нем строк и столбцов,
# print(data.shape) 
# print(data)
# print(data.dtypes) #определить какой тип данных имеют столбцы
# print(data.info()) #инфа по таблице
# print(data.describe()) # общая инфа по таблице

"""
1. Проверить есть ли в файле пустые значения
2. Показать median_house_value где median_income < 2
3. Показать данные в первых 2 столбцах
4. Выбрать данные где housing_median_age < 20 и
median_house_value > 70000
"""
# from pandas import read_csv
# data = read_csv('california_housing_test.csv')
# print(data.isnull()) #Проверить есть ли в файле пустые значения
# print(data.isnull().sum()) #выводим сумму нулевых значений (если они есть)
# print(data[data['housing_median_age'] < 2]['median_house_value']) # Показать median_house_value где median_income < 2
# print(data[["longitude", "latitude"]]) #Показать данные в первых 2 столбцах
# print(data.iloc[:, :2]) #Показать данные в первых 2 столбцах при учете того что мы не знаем наименование столбцов
# print(data["housing_median_age"] < 20) & (data["median_house_value"] > 70000) #Выбрать данные где housing_median_age < 20 и median_house_value > 70000


"""
1. Определить какое максимальное и минимальное
значение median_house_value
2. Показать максимальное median_house_value, где
median_income = 3.1250
3. Узнать какая максимальная population в зоне
минимального значения median_house_value
"""
# from pandas import read_csv
# data = read_csv('california_housing_test.csv')
# print(data["median_house_value"].max(), data["median_house_value"].min()) #Определить какое максимальное и минимальное значение median_house_value
# print(data[data["median_income"] == 3.1250]["median_house_value"].max()) #Показать максимальное median_house_value, где median_income = 3.1250
# print(data[data['median_house_value'] == data['median_house_value'].min()]['population'].max()) #Узнать какая максимальная population в зоне минимального значения median_house_value



