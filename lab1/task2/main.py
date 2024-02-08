import random

#3 Дана строка в которой слова записаны через пробел. Необходимо
# перемешать все слова этой строки в случайном порядке.
def peremesh(a):
    a = a.split(' ')
    for i in range(len(a)):
        b = a[i]
        c = random.randint(0,len(a)-1)
        a[i] = a[c]
        a[c] = b
    return a


# 8 Дана строка в которой записаны слова через пробел. Необходимо
# посчитать количество слов с четным количеством символов.
def kol(a):
    kol = 0
    a = a.split(' ')
    for i in range(len(a)):
        if len(a[i]) % 2 == 0:
            kol += 1
    return kol


print('Введите строку для задачи 1:')
a = input()
print(peremesh(a))

print('Введите строку для задачи 2:')
a = input()
print(kol(a))
