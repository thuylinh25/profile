# https://www.hackerrank.com/challenges/predicting-house-prices/problem

import numpy as np
from sklearn.linear_model import LinearRegression

F, N = map(int, input().split(" "))
data = np.array([input().split() for _ in range(N)], float)
X_train = data[:,:-1]
y = data[:,-1]
T = int(input())
X_test = np.array([input().split() for _ in range(T)], float)

model = LinearRegression()
model.fit(X_train,y)
results = model.predict(X_test)
for i in range (len(results)):
    print(round(results[i],2))
   