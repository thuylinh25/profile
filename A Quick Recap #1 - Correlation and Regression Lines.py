# https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem
# Cach 1
from scipy.stats import pearsonr
physics_scores =[15,12,8,8,7,7,7,6,5,3]
history_scores = [10,25,17,11,13,17,20,13,9,15]
corr,_ = pearsonr(physics_scores, history_scores)
print('Pearsons correlation:%.3f' % corr)

# Cach 2
import math

physics_scores =[15,12,8,8,7,7,7,6,5,3]
history_scores = [10,25,17,11,13,17,20,13,9,15]

def covariance(a, b):
    if len(a) != len(b):
        return
    a_mean = sum(a)/float(len(a))
    b_mean = sum(b)/float(len(b))
    sub = 0
    for i in range(0, len(a)):
        sub += ((a[i] - a_mean) * (b[i] - b_mean))
    return sub/(len(a)-1)


cov = covariance(physics_scores, history_scores)

def standard_deviation(data):
    n = len(data)
    mean = sum(data) / n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / (n-1)
    standard_deviation = math.sqrt(variance)
    return standard_deviation

physics_std = standard_deviation(physics_scores)
history_std = standard_deviation(history_scores)
r = cov/(physics_std * history_std)
print('Pearsons correlation:%.3f' % r)
