from sklearn.preprocessing import Normalizer
from numpy import loadtxt
import numpy as np
import matplotlib as plt 
import pandas as pd
from numpy import reshape

data = loadtxt('data-time.txt')
print(data)
#redata = np.reshape(-1,1)
#print(redata)
scaler = Normalizer()
print(scaler.fit(data))
Normalizer(norm='max',copy=True)
print(scaler.norm)
a = scaler.transform(data)
np.savetxt('data-time-scaler.txt', a)
print(a)

#print(scaler.transform([[2, 2]]))
