# You are given an array of N integers separated by spaces, all in one line.
# Display the following
# 1.Mean (m): The average of all the integers.
# 2.Median of this array: In case, the number of integers is odd, the middle element; else, the average of the middle two elements.
# 3.Mode: The element(s) which occurs most frequently. If multiple elements satisfy this criteria, display the numerically smallest one.
# 4.Standard Deviation (SD).
# SD = (((x1-m)2+(x2-m)2+(x3-m)2+(x4-m)2+...(xN-m)2))/N)0.5
# where xi is the ith element of the array
# 5.Lower and Upper Boundary of the 95% Confidence Interval for the mean, separated by a space.

N = int(input("Number of integer:"))
# array = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]
# print(array[1])
list = []
for i in range(0, N):
    ele = int(input())
    list.append(ele)

def mean():
    mean = sum(list)/N
    return round(mean,2)
print(mean())
def median():
    sorted_list = sorted(list)
    index = N//2
    if N%2 != 0:
        return sorted_list[N/2]
    return sum(sorted_list[index-1:index+1])/2
print (median())
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
import math
def standard_deviation():
    mean = sum(list) /N
    deviations = [(x - mean) ** 2 for x in list]
    variance = sum(deviations) / (N-1)
    standard_deviation = math.sqrt(variance)
    return '%.2f' % standard_deviation
print(standard_deviation())




# array = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]