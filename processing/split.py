from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np  

fname = "sent2.txt"
num_lines = sum(1 for line in open(fname));
embedded_vector = np.zeros((num_lines,100),dtype = np.float);
k = 0
with open(fname, "r") as ins:
    for line in ins:
        a =[float(i) for i in line.split(' ')]
        embedded_vector[k,0:100] = a
        k = k+1
with open('output_split_vector.txt', 'w') as f:
    f.write(str(embedded_vector))
    f.close()
print(embedded_vector)


