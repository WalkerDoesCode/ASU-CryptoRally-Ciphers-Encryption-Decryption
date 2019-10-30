'''
Author: Walker Kroubalkian
Implementation of RSA Cipher Encryption in Python 2.7
'''

import time

message = 37
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

def RSAEncrypt(m,N,e):
    return squareMultiply(m, e, N)

start = time.time()
print RSAEncrypt(message, N, e)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

27
--- 1.59740447998e-05 seconds ---

for input of message = 37, N = 55, e = 17.
'''