 # https://www.hackerrank.com/challenges/battery/problem?fbclid=IwAR3V0KeFoxvXfWnEfLjiesjaKSrkPTTTr9pmWrYovEsaqtl1XLXQaVMraN8
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv('https://s3.amazonaws.com/hr-testcases/399/assets/trainingdata.txt', header = None)
data.columns = ['charge time','last']
charge_time = data['charge time']
battery_time = data['last']

maxIndex=[]
feats=[]
for x in range(len(battery_time)):
    if battery_time[x]==8.0:
        maxIndex.append(x)

for idx in maxIndex:
    feats.append(charge_time[idx])
min_c_time=min(feats)
linFeats=[]
idxlinFeats=[]
linTargets=[]
for idxFeat in range(len(charge_time)):
    feat=charge_time[idxFeat]
    if feat<min_c_time:
        linFeats.append(feat)
        idxlinFeats.append(idxFeat)
for idx in idxlinFeats:
    linTargets.append(battery_time[idx])
linFeats = np.array(linFeats)
linFeats = linFeats.reshape(-1,1)
linTargets = np.array(linTargets)
linTargets = linTargets.reshape(-1, 1)

timeCharged = float(input())
linModel=LinearRegression()
linModel.fit(linFeats,linTargets)
prediction=linModel.predict([[timeCharged]])
prediction=prediction[0]
if prediction>8.0:
    print('8.00')
else:
    result = list(prediction)
    print('%.2f'%result[0])
