import checkTime as ct
import getMention as gm
import numpy as np
import random
def countWord(str):
    senNum = []
    isTime = []
    menNum = []
    with open(str) as f:
        for line in f:
            if(line=='\n'):
                continue
            if (line[31] == ':'):
                line = line[32:]
            menNum.append(gm.getMetion(line))
            senNum.append(len(line.split())-1)
            if(len(ct.timeCheck(line))==0):
                isTime.append(0)
            else:
                isTime.append(0.5)
    return senNum, isTime, menNum


#a, a2 = countWord("FoodyChat.txt")
#b, b2 = countWord("AppointmentChat.txt")
#c, c2 = countWord("TechnoChat.txt")

#print(np.stack((a,a2)))
#print(np.stack((b,b2)))
#print(np.stack((c,c2)))

a, a2, a3 = countWord("data-raw.txt")
np.savetxt('word_count.txt',a,fmt='%d')
np.savetxt('mention.txt',a3,fmt='%d')
np.savetxt('check_time.txt',a2,fmt='%.1f')
#np.savetxt()
print(a, len(a))
print(a2, len(a2))
print(a3, len(a3))