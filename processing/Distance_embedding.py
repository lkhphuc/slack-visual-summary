import __future__
import numpy as np 
import pandas as pd 
import scipy as sp
from scipy.spatial.distance import cosine
with open("sent_embedding.txt","r") as f:
    line_num = sum(1 for line in f)
print(line_num)

matrix_embedding = np.empty([line_num,line_num])

x =np.loadtxt("sent_embedding.txt",dtype=float)
print(x[1])
for i in range(0,line_num):
    a = x[i]
    print('a = %d',i)
    for j in range(0,line_num):
        b = x[j]
        dist = cosine(a,b)
        print(dist)
        matrix_embedding[i,j] = dist
np.savetxt('matrix_embedding.txt',matrix_embedding,fmt='%.8f')