'''
Author: Walker Kroubalkian
Implementation of RSA Cipher Decryption in Python 2.7
'''

import time
from math import sqrt

cipherText = 37
N = 55
e = 17

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

def factorRSA(N):
    upper = int(sqrt(N))
    if(N%2==0):
        return [2,N/2]
    for p in range(3,upper+1,2):
        if(N%p==0):
            return [p,N/p]
    return [-1,-1]

def modInverse(r,m):
    for i in range(1,m):
        if(r*i%m==0):
            return i
    return -1

def RSADecrypt(c,N,e):
    pq = factorRSA(N)
    if pq[0]==-1:
        return "ERROR: Invalid choice of public key N"
    p = pq[0]
    q = pq[1]
    d = modInverse(e, (p-1)*(q-1))
    return squareMultiply(c, d, N)

start = time.time()
print RSADecrypt(cipherText, N, e)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

37
--- 2.78949737549e-05 seconds ---

for input of cipherText = 37, N = 55, e = 17.
'''