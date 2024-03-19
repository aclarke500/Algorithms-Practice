import math


def caller(n):
    table = [None] * n
    return (seq(n, table), table)


def seq(n, table):
    if n == 1:
        return 0
    if not int(n) == n:
        return math.inf
    n = int(n)
    if table[n - 1]:
        return table[n - 1]
    a = seq(n - 1, table)
    b = seq(n / 2, table)
    c = seq(n / 3, table)
    print(f'For {n} we have {a}, {b}, {c}.')
    opt = min(a,b,c)
    table[n-1] = opt + 1
    return opt + 1

print(caller(10))
