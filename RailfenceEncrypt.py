'''
Author: Walker Kroubalkian
Implementation of Railfence Cipher Encryption in Python 2.7
'''

import time

message = "anewsemesterbeginswithfootballandmovingvans"
key = 5

def railfenceEncrypt(m,k):
    rows = []
    for _ in range(k):
        rows.append([])
    increasing = True
    i = 0
    t = 0
    l = len(m)
    while(t<l):
        rows[i].append(m[t])
        if increasing:
            i+=1
        else:
            i-=1
        if(i==0 or i==k-1):
            increasing = not increasing
        t+=1
    s = ""
    for x in rows:
        for y in x:
            s+=y
    return s

start = time.time()
print railfenceEncrypt(message, key)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

asnodanetisotnmvnemegwfbaogswereihalvnsbtli
--- 2.71797180176e-05 seconds ---

for input of message = 'anewsemesterbeginswithfootballandmovingvans', key = 5.
'''