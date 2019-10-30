'''
Author: Walker Kroubalkian
Implementation of Hill Cipher Decryption with Key in Python 2.7
'''

import time
from numpy import array
from numpy.linalg import inv, det

cipherText = "EMRISXCAEGOHJEVI"
key = [[2,7],[5,22]]

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

def modInverse(r,m):
    for i in range(1,m):
        if(i*r%m==1):
            return i
    return -1

def invertMatrix(a):
    d = abs(int(round(det(a))))
    b = inv(a)*d*modInverse(d%26, 26)
    b%=26
    c = []
    for x in b:
        c.append(map(int,map(round,x)))
    return c

def hillDecrypt(c,k):
    c = c.lower()
    l = len(k)
    realCipher = textToHillArray(c, l)
    a = array(k)
    c = invertMatrix(a)
    s = ""
    v = ord("a")
    for x in realCipher:
        for i in range(l):
            w = 0
            for j in range(l):
                w+=x[j]*c[j][i]
            s+=chr(v+(w%26))
    return s

start = time.time()
print hillDecrypt(cipherText, key)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

goodluckseniorsx
--- 0.000172853469849 seconds ---

for input of given cipher text and key of [[2,7],[5,22]].
'''