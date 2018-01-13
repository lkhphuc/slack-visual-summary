from sklearn.preprocessing import MinMaxScaler
from numpy import loadtxt
import numpy as np
import matplotlib as plt 
import pandas as pd
from numpy import reshape

data = loadtxt('data-time.txt')
print(data)
#redata = np.reshape(-1,1)
#print(redata)
scaler = MinMaxScaler()
print(scaler.fit(data))
MinMaxScaler(copy=True, feature_range=(0, 100))
print(scaler.data_max_)
a = scaler.transform(data)
np.savetxt('time-scale.txt', a,fmt='%.6f')
print(a)

#print(scaler.transform([[2, 2]]))
