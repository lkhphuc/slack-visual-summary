import __future__
import numpy as np 
import pandas as pd 

with open("data-time-scaler.txt","r") as f:
    line_num = sum(1 for line in f)
print(line_num)
data = np.genfromtxt('data-user.txt',dtype='str')
print (data)

            
