# https://www.hackerrank.com/challenges/stat-warmup/problem
# cach 1
import math

N=int(input())
list = list(map(int, input().split()))

mean = sum(list)/N
print(round(mean,1))

sorted_list = sorted(list)
index = N//2
if N%2 != 0:
    print (sorted_list[N/2])
else:
    print(sum(sorted_list[index-1:index+1])/2)

def mode():
     sorted_list = sorted(list)
     new_list = []
     i = 0
     while i < N:
         new_list.append(sorted_list.count(sorted_list[i]))
         i += 1
     d1 = dict(zip(list, new_list))
     d2 ={k for (k,v) in d1.items() if v == max(new_list)}
     mode = min(d2)
     return mode
print(mode())

mean = sum(list) /N
deviations = [(x - mean) ** 2 for x in list]
standard_deviation = (sum(deviations) / N)**0.5
print('%.1f'%standard_deviation)

sqrt_sample_size = math.sqrt(N)
a = round(mean - (1.96 * (standard_deviation/sqrt_sample_size)),1)
b = round(mean + (1.96 * (standard_deviation/sqrt_sample_size)),1)
print(a,b)

# cach 2
import numpy as np
import math
from scipy import stats
n = int(input())
arr = np.array([input().split()], dtype=int)
print("{0:.1f}".format(np.mean(arr)))
print("{0:.1f}".format(np.median(arr)))
print(stats.mode(arr, axis=None)[0][0])
print("{0:.1f}".format(np.std(arr)))
cf2 = np.mean(arr) + (1.96 * (np.std(arr) / math.sqrt(n)))
cf1 = np.mean(arr) - (1.96 * (np.std(arr) / math.sqrt(n)))
print('{:.1f}'.format(cf1), '{:.1f}'.format(cf2))
