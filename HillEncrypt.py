'''
Author: Walker Kroubalkian
Implementation of Hill Cipher Encryption in Python 2.7
'''

import time

message = "timetostudy"
key = [[1,4,0],[7,11,2],[0,5,1]]

def textToHillArray(m,l):
    v = ord("a")
    total = []
    i = 0
    while(i<len(m)-l):
        new = []
        for x in range(l):
            new.append(ord(m[i+x])-v)
        total.append(new)
        i+=l
    if(i!=len(m)):
        new = []
        for x in range(i,len(m)):
            new.append(ord(m[x])-v)
        while(len(new)<l):
            new.append(23)
        total.append(new)
    return total

def hillEncrypt(m,k):
    l = len(k)
    total = textToHillArray(m, l)
    final = []
    for x in total:
        row = []
        for i in range(l):
            v = 0
            for j in range(l):
                v+=x[j]*k[j][i]
            v%=26
            row.append(v)
        final.append(row)
    v = ord("a")
    s = ""
    for x in final:
        for y in x:
            s+=chr(v+y)
    return s
    

start = time.time()
print hillEncrypt(message, key)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

xqchjavrgpbt
--- 4.38690185547e-05 seconds ---

for input of message = 'timetostudy', key = [[1,4,0],[7,11,2],[0,5,1]].
'''