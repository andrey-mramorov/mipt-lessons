from math import sqrt
lst = list(map(int, input().split()[:-1]))

max_lst = max(lst)
min_lst = min(lst)
avg_lst = sum(lst) / len(lst)
dsp = 0

for x in lst:
    dsp += (x - avg_lst)**2

avg_dsp = sqrt(dsp / len(lst))

print(lst)
