import __future__
import numpy as np 
import pandas as pd 



with open("data-time.txt","r") as f:
    line_num = sum(1 for line in f)
print(line_num)

matrix_time = np.empty([line_num,line_num])
x =np.loadtxt("data-time.txt",dtype=float)
print(x[1])
for i in range(0,line_num):
    a = x[i]
    for j in range(0,line_num):
        b = x[j]
        dist = abs(a-b)
        print(dist)
        matrix_time[i,j] = dist
np.savetxt('matrix_time.txt',matrix_time,fmt='%.8f')

        
