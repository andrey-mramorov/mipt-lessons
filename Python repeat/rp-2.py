def quick_sort(x, low, high):
    if low < high:
        p = len(x) // 2
        x = x[:low] + list(filter(lambda x: x < x[p], x[low:high])) + list(filter(lambda x: x >= x[p], x[low:high])) + x[high:]
        quick_sort(x, low, p-1)
        quick_sort(x, p+1, high)

import numpy as np

x = list(np.random.randint(100, size=100))

print(quick_sort(x, 0, len(x)))

