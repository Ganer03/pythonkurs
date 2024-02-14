# 9 Дан целочисленный массив. Необходимо
# найти элементы, расположенные перед последним минимальным.
def f1(a):
    b = min(a)
    index = len(a) - 1 - a[::-1].index(b)
    return a[0:index]


# 21 Дан целочисленный массив.
# Необходимо найти элементы,
# расположенные после первого максимального.
def f2(a):
    b = max(a)
    print(b)
    index = a.index(b)
    print(index)
    return a[index+1:len(a)-1]


# 33 Дан целочисленный массив. Проверить, чередуются ли в нем
# положительные и отрицательные числа.
def f3(a):
    is_alternating = True
    for i in range(1, len(a)):
        if a[i - 1] < 0 and a[i] > 0:
            is_alternating = True
        elif a[i - 1] > 0 and a[i] < 0:
            is_alternating = True
        else:
            is_alternating = False
            break
    return is_alternating


a = input('Введите элементы массива в строку через пробел: ')
a = a.split()
a = [int(item) for item in a]
print('Элементы, расположенные перед последним минимальным: ',f1(a))
print('Элементы, расположенные после первого максимального: ',f2(a))
print('Чередуется: ', f3(a))


