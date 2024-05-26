""" 
Задача №1. Ввод-вывод, операторы ветвления.
За день машина проезжает n километров. Сколько
дней нужно, чтобы проехать маршрут длинной m
километров? При решении задачи нельзя пользоваться 
условной инструкцией if и циклами

input:
n = 700
m = 750

Output:
2
"""
# from math import ceil #Нужно сделать округление до ближайшего максимального целого
# m, n = 750, 700 #поэтому используем модуль math и его функцию ceil
# print(ceil(m / n))
# print((m + n - 1) // n) #Чтобы получить целочисленное, чтобы получить верное решение вычитаем 1

'''
Задача №3.
В некоторой школе решили набрать три новых
математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть
два учащихся. Известно количество учащихся в
каждом из трех классов. Выведите наименьшее
число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32
'''
# a, b , c = 20, 21, 22 #Присваивание через запятую называется присваивание через кортеж
# print(a // 2 + a % 2 + b // 2 + b % 2 + c // 2 + c % 2) #a//2 норма если 20 детей, а если 21 то деление с остатком поэтому делим на %
# #Далее добавим пояснение в вывод через формат f 
# print(f"Общее число парт: {a // 2 + a % 2 + b // 2 + b % 2 + c // 2 + c % 2}")

"""
Задача №5
Вагоны в электричке пронумерованы
натуральными числами, начиная с 1 (при этом иногда
вагоны нумеруются от «головы» поезда, а иногда – с
«хвоста»; это зависит от того, в какую сторону едет
электричка). В каждом вагоне написан его номер.
Витя сел в i-й вагон от головы поезда и обнаружил,
что его вагон имеет номер j. Он хочет определить,
сколько всего вагонов в электричке. Напишите
программу, которая будет это делать или сообщать,
что без дополнительной информации это сделать
невозможно.
Input: 3 4(ввод на разных строках)
Output: 6
"""

# i, j = 3, 4
# if i != j: #Если i не равно j, то решение есть тогда мы понимаем - находимся не в среднем вагоне
#     print(i + j - 1) # - 1 т.к. чтобы не счить вагон в котором сидим дважды
# else: #иначе то
#     print("Задача не решаема")


"""
Задача №7
Дано натуральное число. Требуется определить,
является ли год с данным номером високосным. Если
год является високосным, то выведите YES, иначе
выведите NO. Напомним, что в соответствии с
григорианским календарем, год является
високосным, если его номер кратен 4, но не кратен
100, а также если он кратен 400.
Input: 2016
Output: YES
"""

# year = int(input("Введите год ")) #input строка a int преобразование строки в числа
# if year % 4 == 0 and year % 100 or year % 400 == 0: #если он делиться на 4 без остатка, и не кратен 100, а так же если он кратен 400 то (то это двоеточие)
#     print("Год високосный")
# else: #или то
#     print("Не високосный")

## Решение через тернарный оператор

# print("Год високосный" if year % 4 == 0 and year % 100 or year % 400 == 0 else "Не високосный")

### ЦИКЛЫ
# while - его смысл в предъиспользовании, сначало деньги потом стулья.
# сначало условие, а потом выполняется действие.

# a = 5
# while a > 0:  ## пока a > 0 то выполняется 
#     print(a)
#     a -= 1    ## уменьшение а на 1 по циклу

### добавим break - остановку цикла

# a = 5
# while a > 0:
#     print(a)
#     if a == 3:  ## Если а станотся равное 3 то выполняется команда break
#       break
#     a -=1 

### В цикле while можно поставить else, если не будет выполняться условие по brek

# a = 2            ## а = 2
# while a > 0:     ## пока а > 0 
#     print(a)     ## мы выводим а
#     if a == 3:   ## как только а станет =3
#         break    ## выполнится команда break
#     a -= 1       ## шаг уменьшения а = 1 т.е. значение а уменьшается на 1, пока не выполняться условия
# else:            ## (или) добавляем если не выполняется команда break
#     print("Завершение цикла по break") ## вывод

## Так-же есть цикл for - необходим для обхода массивов н-р строка (она же является массивом)

### Сделавем обход(перечисление) значений строки

# my_str = "xldkrit"       ## объявим строку my_str
# for el in my_str:        ## вводим переменную el. для переменной el в строке my_str. i- это переменная которая обычно используется для индекса, поэтому переменная el
#     print(el, end=" ")   ## вывести по отдельности значения, end=" " добавили, чтобы все выводилось в одну строку вместо столбца
# ## далее добавим обход по индексу через цикл while
# i = 0           ## добавляем переменную индекса i
# while i < len(my_str): ## условие по i меньше длины строки (метод len строки my_str len(my_str) метод от слова lenght-длина)
#     print(my_str[i])   ## выводим i-тый элемент индекса из строки my_str, (можем добавить end) print(my_str[i], end=" ")
#     i += 1             ## шаг изменения индекса +1

## Цикл while подойдет когда не знаешь число итерации