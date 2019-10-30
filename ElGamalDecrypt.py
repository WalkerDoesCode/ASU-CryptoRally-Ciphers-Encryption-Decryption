'''
Author: Walker Kroubalkian
Implementation of El Gamal Cipher Decryption in Python 2.7
'''

import time

r = 137
t = 229
p = 257
alpha = 3
beta = 112

def squareMultiply(b,e,m):
    l = len(bin(e)[2:])
    power = b
    powers = []
    for _ in range(l):
        powers.append(power)
        power*=power
        power%=m
    v = bin(e)[2:][::-1]
    total = 1
    for i in range(l):
        if v[i] == "1":
            total*=powers[i]
            total%=m
    return total

def modInverse(r,m):
    for i in range(1,m):
        if(i*r%m==1):
            return i
    return -1

def discreteLog(b,r,m):
    power = b%m
    e = 1
    while(power!=r and e<m):
        power*=b
        power%=m
        e+=1
    if(e!=m):
        return e
    return -1

def elGamalDecrypt(r,t,p,a,b):
    a = discreteLog(a, b, p)
    base = modInverse(r,p)
    m = squareMultiply(base, a, p)*t%p
    return m

start = time.time()
print elGamalDecrypt(r,t,p,alpha,beta)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

138
--- 4.2200088501e-05 seconds ---

for input of r = 137, t = 229, p = 257, alpha = 3, beta = 112.
'''