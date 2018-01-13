import __future__
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.preprocessing import normalize
from sklearn.cluster import SpectralClustering
from sklearn.cluster import DBSCAN

w1 = np.loadtxt('matrix_embedding.txt',dtype=float)
w2 = np.loadtxt('matrix_time.txt',dtype=float)

print(w1.shape)
print(w2.shape)
ld1 = 1
ld2 = 0.01
ld3 = 1

w1ld1 = np.multiply(ld1,w1)
w2ld2 = np.multiply(ld2,w2)

np.savetxt('w1ld1.txt',w1ld1,fmt='%.6f')
np.savetxt('w2ld2.txt',w2ld2,fmt='%.6f')

sum_w = np.add(w1ld1,w2ld2)
#print (sum_weight)
np.savetxt('sum_weight.txt', sum_w,fmt='%.6f')

##Spectral clustering
clus = SpectralClustering(n_clusters=2,affinity='precomputed',
                            assign_labels='discretize')
clus.fit(sum_w)

print('Spectral_predict = ')
print(clus.fit_predict(sum_w))

##DBSCAN

DBcluster = DBSCAN(metric='precomputed')
DBcluster.fit(sum_w)
print('DBSCAN = ')

predict = DBcluster.fit_predict(sum_w)
print(predict)
np.savetxt('cluster_predict.txt',predict,fmt='%d')

## Visualize data color
# plt.imshow(sum_w)
# plt.show()


