## Seminar 4
"""
Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
"""
# data = "a a a b c a a d c d d"
# res = {}
# for item in data:
#     if item not in res:
#         print(item, end=" ")
#     else:
#         print(f"{item}_{res[item]}", end=" ")
#     res[item] = res.get(item, 0) + 1 

# data = "a a a b c a a d c d d".split()
# res = {}
# for item in data:
#     if item not in res:
#         print(item, end=" ")
#     else:
#         print(f"{item}_{res[item]}", end=" ")
#     res[item] = res.get(item, 0) + 1

"""
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore
I'm sure that the shells are sea shore shells
Output: 13
"""

# data = """She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells""".lower().split()
# print(len(set(data)))

data = """She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells""".lower().split()
print(len(list(set(data))))


"""
Задача №29. Решение в группах
Ваня и Петя поспорили, кто быстрее решит
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не
такими смышлеными. Никто из ребят не смог до
конца сделать это задание. Они решили так: у кого
будет меньше ошибок в коде, тот и выиграл спор. За
помощью товарищи обратились к Вам, студентам.


Ваня:

n = int(input())
max_number = 1000
while n != 0:
n = int(input())
if max_number > n:
max_number = n
print(max_number)

Петя:

n = int(input())
max_number = -1
while n < 0:
n = int(input())
if max_number < n:
n = max_number
print(n)
"""
#Обычное решение 
# n = int(input())
# max_nuber = n
# while n != 0:
#     n = int(input())
#     if max_nuber < n:
#         max_nuber = n
# print(max_nuber)

#решение с рекурсией
# def func(n, max_number):
#     if n == 0:
#         return max_number
# n = int(input())
# if max_number < n:
#     max_number = n
#     return func(n, max_number)

# n = int(input())
# print(func(n, n))

"""
Задача препда
"""
# for i in 'hello world':
#     if i == 'a':
#         break
# else:
#     print('Буквы a в строке нет')

# def func(my_str='hello worlda'):
#     if len(my_str) != 0:
#         if my_str[0] == 'a':
#             return
#     else:
#         func(my_str[1:])
# else:
# print('Буквы a в строке нет')

# func()