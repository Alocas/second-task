def permutation(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in permutation(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


def swap(n):
    k = 0
    zero = ''
    number = ''
    for i in range(n + 1):
        if i != n:
            zero += '0'
        if i != 0:
            number += str(i)

    mass = []

    for i in permutation(zero + number):
        mass.append(i)
    file = open('result.txt', 'w+')
    flag = 1
    while flag == 1:
        for i in range(len(mass)):
            a = mass.count(mass[i])
            while a > 1:
                del mass[i]
                a -= 1
                mass.append('')
            else:
                flag = 0
    flag2 = 1
    while flag2 == 1:
        for i in range(len(mass)):
            for g in range(len(mass)):
                if mass[i] == mass[g]:
                    del mass[g]
                    mass.append('')
                else:
                    flag2 = 0
    for i in range(len(mass)):
        if mass[i] != '':
            file.write(str(mass[i]) + '\n')
            k += 1
    print('Strings - ', k)


swap(7)
