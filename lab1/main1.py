//zad1
//функция 1
def max_easy_del(a):
    delitel = 0
    for i in range(2, a):
        if a % i == 0:
            delit = 0
            for j in range(2, i):
                if i % j == 0:
                    delit += 1
            if delit == 0:
                delitel = i
    return delitel

print('Введите число')
a = int(input())
max = max_easy_del(a)
print('max_del_prost: ', max)
