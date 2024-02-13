# 3 Дана строка. Необходимо найти общее количество русских символов.
def kol(a):
    r = 0
    for i in range(0, len(a)):
        if 1072 <= ord(a[i]) <= 1102:
            r += 1
    print(r)


a = input()
kol(a)
