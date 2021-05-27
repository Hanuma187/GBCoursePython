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