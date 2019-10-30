'''
Author: Walker Kroubalkian
Implementation of Vigenere Cipher Encryption in Python 2.7
'''

import time

message = "genekellysdance"
key = "rain"

def vigenereEncrypt(m,k):
    s = ""
    v = ord("a")
    i = 0
    l = len(k)
    for x in m:
        w = ord(k[i])-v
        s+=chr(v+(ord(x)-v+w)%26)
        i+=1
        i%=l
    return s
    

start = time.time()
print vigenereEncrypt(message, key)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

xevrbetypslnecm
--- 1.59740447998e-05 seconds ---

for input of message = 'genekellysdance', key = 'rain'.
'''