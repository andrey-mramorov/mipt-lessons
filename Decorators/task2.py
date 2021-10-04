def dec_for_func(func):
    def wrapper(lst):
        value = func(lst)
        if value == 0:
            print('Нет')
        elif value > 10:
            print('Очень много')
        else:
            print(value)

    return wrapper
        
@dec_for_func
def chetnost(lst):
    cnt = 0
    for number in lst:
        if number % 2 == 0:
            cnt += 1
    return cnt

