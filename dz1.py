# Домашнее задание 1
# _1._
a=2
b=7
c='mam'
print(a)
print(b)
print(c)

# _2._
seconds=int(input("Введите время в секундах"))
h = seconds // 3600
m = seconds % 3600 // 60
s = seconds % 3600 % 60
print("часы:минуты:секунды "+'{}:{}:{}'.format(h, m, s))

# _3._
n=int(input("Введите число n "))
print("n + nn + nnn = "+str(n+n*n+n*n*n))


#_4._
number=int(input("Введите целое число "))
maxik = number % 10
while number > 10:
    f = number % 10
    number //= 10
    if f > maxik:
        maxik = f
print("Максимальная цифра: "+ str(maxik))

#6._
vyru4ka=int(input("Введите прибыль фирмы: "))
izderjxki=int(input("Введите издержки фирмы: "))
if vyru4ka>izderjxki:
    pribyl=vyru4ka-izderjxki
    print("Прибыль: " + str(pribyl))
    rentabelnostj=pribyl/vyru4ka
    print("Рентабельность:" + str(rentabelnostj))
    number=int(input("Введите число сотрудников:"))
    pribyl2worker=rentabelnostj/number
    print("Прибыль в расчете на сотрудника: " + str(pribyl2worker))
else:
    print ("Убыток")

#_7._
s=int(input("Введите пробег спортсменав в первый день"))
day=1
rez=int(input("Введите желаемый результат"))
while rez>s:
    s *= 1.1
    day += 1
    print(str(day)+"ий день, " + str("{:.2f}".format(s)))
print("Желаемый результат достигнут.")
