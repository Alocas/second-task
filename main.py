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

    f = open('res.txt', 'w+')
    for i in permutation(zero + number):
        f.write(i + '\n')
        k += 1

    f.close()
    print('Strings - ', k)


swap(7)
