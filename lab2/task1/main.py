def main():
    filename = "input.txt"
    language = {}
    max = 0
    b = []
    with open(filename, 'r') as file:
        n = int(file.readline())
        for i in range(0,n):
            list = file.readline().strip('\n')
            if list.isdigit():
                j = int(list)
                i += j+1
                c = []
                for k in range(0,j):
                    list = file.readline().strip('\n')
                    if list in language:
                        language[list] += 1
                    else:
                        language[list] = 1
                    c.append(list)
                if j>max:
                    max = j
                    b = c
    count = 0
    list = []
    print(language)
    for i in language:
        if language[i] == n:
            list.append(i)
            count += 1
    print(count)
    for i in range(len(list)):
        print(list[i])
    print(max)
    b.sort()
    for i in b:
        print(i)


if __name__ == "__main__":
    a = {}
    main()