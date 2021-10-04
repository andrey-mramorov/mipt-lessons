import time
import numpy as np

def dec_with_args(file_path):
    
    def decorator(func):
        
        def wrapper(*args):
            arguments = list(args)
            func_call = time.time()
            func_ans = func(*args)
            func_end = time.time()
            
            with open(file_path, 'a') as file:
                file.write('--Тест--\n')
                file.write('Время вызова функции: ' + str(func_call) + '\n')
                file.write('Аргументы функции: ' + ' '.join(map( str, arguments )) + '\n')
                if func_ans == None:
                    file.write('Ответ return: ' + '-' + '\n')
                else:
                    file.write('Ответ return: ' + str(func_ans) + '\n')
                file.write('Время завершения работы функции: ' + str(func_end) + '\n')
                file.write('Время работы функции: ' + str(func_end - func_call) + '\n\n')
            
            #return func(*args)
        return wrapper
    return decorator
                
@dec_with_args('test_log.txt')
def test_func(arr):
    return sorted(arr)

print('Логгирование функции sorted()\n\nВведите число элементов для массива случайных чисел: ')
N = int(input())

arr = list(np.random.rand(N) * 50)
#print(arr, '\n')
test_func(arr)

