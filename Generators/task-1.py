def print_map(func, iterable):
    for i in iterable:
        print(func(i))


def f(elem):
    return elem**2

l = [3, 4, 7, 5]

print_map(f, l)

def p_map(func, iterable):
    i = iter(iterable)
    try:
        while True:
            print(func(next(i)))
    except:
        pass


p_map(f, l)
