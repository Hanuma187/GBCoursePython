"""
Задание 1 про зарплату
"""
def oplata():
    x = int(input('Сколько часов отработано?  '))
    y = int(input('Какой размер оплаты за час?  '))
    c = int(input('Размер премии - '))
    pay = x * y
    return pay + c
print(f'Размер заработной платы составил: {oplata() }')

"""
Задание 2 о порядке чисел
"""
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new = [my_list[i] for i in range(1, len(my_list))  if my_list[i] > my_list[i - 1]]
print(new)


"""
Задание 3 о числах
"""
randomi = range(20, 241)
print(randomi)
new_num = [el for el in randomi if el%20==0 or el%21==0]
print(f'Из них кратны 20 и 21: {new_num }')

"""
Задание 4 о неповторяющихся числах
"""

from functools import reduce


rez = reduce(lambda x, i: x * i, range(100, 1001, 2))
print('Произведение ', rez)

"""
Задание 5 об итераторах
"""

from itertools import islice
from itertools import count
from itertools import cycle

def my_count_func(start_number, iter_number):
    for i in islice(count(start_number), iter_number):
        print(i)

def my_cycle_func(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i+=1

my_count_func(start_number = int(input("Введите начальное число: ")), iter_number = int(input(" Введите число итераций: ")))


my_cycle_func(my_list = [1, 2], iteration = int(input("Введите число итераций для повторящихся данных: ")))


"""
Задание 7 о факториале
"""
from math import factorial

def func(n: int):

    for i in range(1, n + 1):
        yield factorial(i)

input_data = input('Число факториалов для вычисления: ')
value = int(input_data)

for el in func(value):
        print(el)

