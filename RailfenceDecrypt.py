'''
Author: Walker Kroubalkian
Implementation of Railfence Cipher Decryption in Python 2.7
'''

import time

cipherText = "BOOIGUYUBOSNUUTYRKAS"
key = 3

def railfenceDecrypt(c,k):
    c = c.lower()
    lc = len(c)
    period = 2*(k-1)
    q = lc/period
    r = lc%period
    rows = []
    t = 0
    for i in range(k):
        if(i==0):
            if(r>0):
                rows.append(c[0:q+1])
                t+=q+1
            else:
                rows.append(c[0:q])
                t+=q
        elif(i==k-1):
            rows.append(c[t:])
        elif(i>=r):
            rows.append(c[t:t+2*q])
            t+=2*q
        elif(r<period-i+1):
            rows.append(c[t:t+2*q+1])
            t+=2*q+1
        else:
            rows.append(c[t:t+2*q+2])
            t+=2*q+2
    rowIndices = []
    for _ in range(k):
        rowIndices.append(0)
    t = 0
    i = 0
    increasing = True
    s = ""
    while(t<lc):
        s+=rows[i][rowIndices[i]]
        rowIndices[i]+=1
        if increasing:
            i+=1
        else:
            i-=1
        if(i==0 or i==k-1):
            increasing = not increasing
        t+=1
    return s

start = time.time()
print railfenceDecrypt(cipherText, key)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

buyyourbooksinaugust
--- 2.00271606445e-05 seconds ---

for input of cipher text = 'BOOIGUYUBOSNUUTYRKAS', key = 3.
'''