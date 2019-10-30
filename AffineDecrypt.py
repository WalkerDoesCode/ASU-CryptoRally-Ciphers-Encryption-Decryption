'''
Author: Walker Kroubalkian
Implementation of Affine Cipher Decryption with Key in Python 2.7
'''

import time

cipherText = "OYHYJLEVYQBLSRIJLYEC"
mu = 5
sh = 4

def modInverse(r,m):
    for i in range(1,m):
        if(r*i%m==1):
            return i
    return -1

def affineDecrypt(c,mu,sh):
    c = c.lower()
    s = ""
    v = ord("a")
    w = modInverse(mu, 26)
    for x in c:
        s+=chr(v+((ord(x)-v-sh)*w)%26)
    return s

start = time.time()
print affineDecrypt(cipherText, mu, sh)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

celebratespringbreak
--- 1.8835067749e-05 seconds ---

for input of cipherText = "OYHYJLEVYQBLSRIJLYEC", mu = 5, sh = 4.
'''