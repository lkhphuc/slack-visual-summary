import json
import numpy as np
import Distance_embedding as de 
import Distance_time as dt 
import random 

sample = {'id': 0, 'time': 0, 'user': '', 'word_count': 0, 'check_time':0, 
            'cluster': 0, 'message':'', 'mention':0}

list_dump = []


# lines = []
with open("matrix_embedding.txt","r") as f:
    line_num = sum(1 for line in f)

time_data = np.loadtxt('time-scale.txt',dtype=float)
user_data = np.genfromtxt('data-user.txt',dtype=str)
cluster_data = np.loadtxt('cluster_predict.txt',dtype=float)
word_num_data = np.loadtxt('word_count.txt',dtype=int)
message = np.genfromtxt('data-text.txt',delimiter='\t',dtype=str)
mention = np.loadtxt('mention.txt',dtype=int)
check_time = np.loadtxt('check_time.txt',dtype=float)
# print(time_data)
# print(user_data)
# print(cluster_data)
# print(word_data)


for i in range(0,line_num):
    print (i)
    sample['id'] = int(i)
    sample['time'] = float(time_data[i])
    sample['user'] = str(user_data[i])
    sample['word_count'] = int(word_num_data[i])
    sample['cluster'] = int(cluster_data[i])
    sample['message'] = str(message[i])
    sample['mention'] = int(mention[i])
    sample['check_time'] = float(check_time[i]+random.uniform(0,0.1))
    list_dump.append(sample.copy())
    #'\n'.join(list_dump)
print (list_dump)
string = "var mysample ="
a = json.dumps(list_dump)
with open('mysample.json','w') as sam:
    sam.write(string)
    sam.write(a)