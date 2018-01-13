from sklearn.preprocessing import StandardScaler
from numpy import loadtxt
import numpy as np
import matplotlib as plt 
import pandas as pd
from numpy import reshape

data = loadtxt('data-time.txt')
print(data)
#redata = np.reshape(-1,1)
#print(redata)
scaler = StandardScaler()
print(scaler.fit(data))
a = scaler.transform(data)
np.savetxt('time-scale.txt', a,fmt='%.6f')
print(a)

#print(scaler.transform([[2, 2]]))
