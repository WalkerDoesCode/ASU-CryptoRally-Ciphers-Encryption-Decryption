'''
Author: Walker Kroubalkian
Implementation of Affine Cipher Encryption in Python 2.7
'''

import time

message = "beach"
mu = 3
sh = 1

def affineEncrypt(m,mu,sh):
    s = ""
    v = ord("a")
    for x in m:
        s+=chr(v+((ord(x)-v)*mu+sh)%26)
    return s

start = time.time()
print affineEncrypt(message, mu, sh)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

enbhw
--- 1.09672546387e-05 seconds ---

for input of message = 'beach', mu = 3, sh = 1.
'''