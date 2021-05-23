#1.
result_list = [6, 'tirlim', 2, complex(3,6),100.3]
print(result_list)
#2
number = int(input("Число членов списка: "))
list_x = []
for num in range(number):
    list_x.append(input("Введите следующий член списка: "))
print(list_x)
j = 0
for i in range(int(len(list_x) / 2)):
    list_x[j], list_x[j + 1] = list_x[j + 1], list_x[j]
    j += 2

print(list_x)
#3
seasons = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}

month = int(input('Введите номер месяца: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)

#4

words = input("Введите строку из слов: ").split()
for ind, word in enumerate(words):
    print(ind, word[:10])

#5
list_x=[]
list_x.append(int(input("Введите первое значение рейтинга: ")))
list_x.append(int(input("Введите второе значение рейтинга: ")))
if list_x[1]>list_x[0]:
    list_x[0], list_x[1] = list_x[1], list_x[0]
print(list_x)
for num in range(100):
    val=int(input("Введите следующий член рейштинга: "))
    max_val = max(list_x)
    min_val = min(list_x)
    if val > max_val:
        list_x.insert(0, val)
    elif val <= min_val:
        list_x.append(val)
    else:
        u=0
        while (list_x[u] >= val) and (list_x[u+1] >= val):
            u = u + 1
        list_x.insert(u+1,val)
    print(list_x)