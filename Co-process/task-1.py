L = [1, 2, 3, 'abc']

L = iter(L)

for i in range(4):
    next(L)
    try:
        L[i] = 0
    except:
        print("нельзя")
