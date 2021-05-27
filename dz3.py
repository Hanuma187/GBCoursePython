#Задание 1
def my_func (x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "y не должно быть равно 0"


A=my_func(int(input("Введите x = ")), int(input("Введите y><0. y = ")))
print(A)

#Задание 2
def my_func(name, surname, year, city, email, phone):
    print(name, surname, year, city, email, phone)

my_func(name= 'Аnna', surname='Fedo', year=1981, city='Chernogolovka', email='email', phone='14563')

#Задание 3
def my_func(x, y, z):
    s = [x, y, z]
    b = sorted(s)
    total = []
    print(b[1]+b[2])
my_func(-4, 2,1)

# Задание 4
def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return print("Степень не отрицательна")
    else:
        return 1 / res

a=int(input("Введите целое число "))
b=int(input("Введите степень (целое отрицательное число)"))
print(power(a,b))

# Задание 5
def my_sum ():
    sum_res = 0
    ex = True
    while ex == True:
        number = input('Введите число или Q для выхода - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = False
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Текущая сумма {sum_res}')
    print(f'Ваша конечная сумма {sum_res}')


my_sum()


#Задание 6

def func(a):
        return a.title()
print(func("hello"))
