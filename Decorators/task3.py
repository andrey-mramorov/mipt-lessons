def swap(func):
    def wrapper(*args):
        #print(type(args), args)
        #func(arg1, arg2, arg3)
        args = tuple([list(args)[1], list(args)[0], list(args)[2]])
        #func(*args)
        return func(*args)
    return wrapper

@swap
def div(x, y, show=False):
    res = x/y
    if show:
        print(res)
    return res

#print(div(4, 2))

div(2, 4, True)

