# https://www.hackerrank.com/challenges/correlation-and-regression-lines-8/problem
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

m = r*(history_std/physics_std)
print('%.3f'%m)

physics_scores_mean = sum(physics_scores)/len(physics_scores)
history_scores_mean = sum(history_scores)/len(history_scores)

y_intercept = history_scores_mean - m*physics_scores_mean
predict_history_score = m*10 + y_intercept
print('%.1f'%predict_history_score)
