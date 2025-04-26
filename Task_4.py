# Функция нахождения корня
def sqrt(a):
    l = 0
    if a >= 1:
        r = a
    else:
        r = 1

    while r - l > 10 ** -5:
        m = (r + l) / 2
        if m ** 2 < a:
            l = m
        else:
            r = m
    return l


# Читаем данные из файла
def create1List():
    lst = []
    with open("CdSe_CdZnS Core_Shell.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            lst.append(float(line.split()[0].replace(',', '.')))
    return lst
def create2List():
    lst = []
    with open("CdSe_CdZnS Core_Shell.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            lst.append(float(line.split()[1].replace(',', '.')))
    return lst

# Функция нахождения среднего отколнения
def averageDeviation(lst, avx):
    summ = 0
    for x in lst:
        summ += abs(x - avx)
    return summ / len(lst)


# Функция нахождения среднеквадратичного отклонения
def standardDeviation(lst, avx):
    summ = 0
    for x in lst:
        summ += (x - avx)**2
    return sqrt(summ / len(lst))


# Присваиваем значения переменным
lst1 = create1List()
lst2 = create2List()
avx1 = sum(lst1) / len(lst1)
avx2 = sum(lst2) / len(lst2)


# Проверяем, всё ли так присвоилось
#print(lst1)
#print(avx1)
#print(lst2)
#print(avx2)


# Ответы:
print("Среднее отклонение первых чисел: ", averageDeviation(lst1, avx1))
print("Среднеквадратичное отклонение первых чисел: ", standardDeviation(lst1, avx1))
print("Среднее отклонение вторых чисел: ", averageDeviation(lst2, avx2))
print("Среднеквадратичное отклонение вторых чисел: ", standardDeviation(lst2, avx2))