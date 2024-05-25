"""Задача 1: Найдите сумму цифр трехзначного числа. 
123 -> 6 (1+2+3) 
100 -> 1 (1+0+0)
"""
### первое решение
# Ввод трехзначного числа
number = int(input("Введите трехзначное число: "))

# Проверка на трехзначное число
if 100 <= number <= 999:
    # Вычисление суммы цифр
    sum_of_digits = number // 100 + (number // 10) % 10 + number % 10
    print(f"{number} -> {sum_of_digits}")
else:
    print("Вы ввели не трехзначное число.")

"""сначала проверяеm, является ли введенное число трехзначным. 
Если да, то он вычисляет сумму его цифр и выводит результат. 
В противном случае, он сообщает, что введено не трехзначное число."""

#В автотестах:
#Найдите сумму цифр трехзначного числа n.
#Результат сохраните в перменную res.

### второе решение для автотестов
n = 123
res = 0

# Разбиваем число на цифры
digit1 = n // 100
digit2 = (n // 10) % 10
digit3 = n % 10

# Суммируем цифры
res = digit1 + digit2 + digit3

print(res)  # Выводит: 6


"""В этом примере мы используем целочисленное деление и остаток от деления для извлечения цифр из трехзначного числа, 
а затем складываем их для получения суммы. 
Результат сохраняется в переменной `res`.
"""
""" 
Задача 2

Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.

Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей.
"""
### Первое решение
def distribute_cranes(n):
    pete = n // 4
    katya = n - pete * 2
    serega = pete
    return f"{pete} {katya} {serega}"

# Пример использования функции
## n = 6
## print(distribute_cranes(n))  # Выводит: 1 4 1

### второе решение

# Вводим общее количество журавликов
n = int(input())

# Рассчитываем количество журавликов, сделанных Петей и Сережей
x = n // 6

# Петя и Сережа сделали одинаковое количество журавликов
print(x, end=' ')

# Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе
print(2 * 2 * x, end=' ')

# Сережа также сделал x журавликов
print(x)

"""
В этом коде мы используем целочисленное деление `//` для определения количества журавликов, 
сделанных Петей и Сережей, которое составляет `n // 6`. Затем мы выводим количество журавликов, 
сделанных Петей, Катей и Сережей, согласно условию задачи.
"""
### Для автотестов
n = int(input())  # Число журавликов

# Вычисляем количество журавликов, сделанных каждым ребенком
petr = n // 6
sergey = petr
katya = 4 * petr

# Выводим результат
print(petr, katya, sergey)

"""
Задача 3
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.

Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.

Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.

Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.

Пример:


n = 385916 -> yes
n = 123456 -> no
"""
# Решение 1 
n = int(input())
digit6 = n // 100000
digit5 = n // 10000
digit4 = n // 1000
digit3 = n // 100
digit2 = (n // 10) % 10 
digit1 = n % 10
if digit1 + digit2 + digit3 == digit4 + digit5 + digit6:
    print("yes")
else:
    print("no")

# Решение 2 через ячейку массива
n = 123321
array = [int(i) for i in str(n)]
sum1 = array[0] + array[1] + array[2]
sum2 = array[3] + array[4] + array[5]
if sum1 == sum2:
    print("yes")
else:
    print("no")

"""
Определите, можно ли от шоколадки размером a x b долек отломить c долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

Выведите yes или no соответственно.

Пример:


a, b, c = 3, 2, 4 -> yes
a, b, c = 3, 2, 1 -> no
"""
#Первый способ
a, b, c = map(int, input().split())

# Проверяем, что c является частью одного из размеров шоколадки
if c % a == 0 or c % b == 0:
    print("yes")
else:
    print("no")

"""
Принимаем на вход три числа a, b и c, используя функцию `input()` и метод `split()` 
для разделения введенной строки на части. 
Затем мы приводим эти части к целочисленному типу с помощь `map()`.

Далее проверяем, что число долек c делится без остатка на один из размеров шоколадки a или b. 
Если это так, выводим "yes", иначе - "no".
"""
#Второй способ
# Ввод значений a, b и c
a = int(input("Введите размер a: "))
b = int(input("Введите размер b: "))
c = int(input("Введите количество долек c: "))

# Проверка возможности отломить c долек
if c % a == 0 or c % b == 0:
    print("yes")
else:
    print("no")
"""
запрашивает у пользователя значения для a, b и c. 
Затем он проверяет, можно ли отломить c долек, 
если разрешается сделать один разлом по прямой между дольками. 
Если c является кратным a или b, то ответ будет "yes", в противном случае - "no".
"""