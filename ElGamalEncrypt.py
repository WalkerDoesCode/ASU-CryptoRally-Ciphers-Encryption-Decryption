'''
Author: Walker Kroubalkian
Implementation of El Gamal Cipher Encryption in Python 2.7
'''

import time

message = 138
p = 257
alpha = 3
beta = 112
k = 72

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

def elGamalEncrypt(m,p,a,b,k):
    r = squareMultiply(a, k, p)
    t = squareMultiply(b, k, p)*m%p
    return [r,t]

start = time.time()
print elGamalEncrypt(message,p,alpha,beta,k)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

[137, 229]
--- 3.00407409668e-05 seconds ---

for input of message = 138, p = 257, alpha = 3, beta = 112, k = 72.
'''