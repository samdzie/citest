def inc(x):
    return x + 1


def fact(x):
    if x < 2:
        return 1
    product = 1
    for i in range(2, x + 1):
        product *= i
    return product


def gcf(x, y):
    factor = 1
    for i in range(1, min(x, y)):
        if x % i == 0 and y % i == 0:
            factor = i
    return factor
