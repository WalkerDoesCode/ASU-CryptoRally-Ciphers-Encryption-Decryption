'''
Author: Walker Kroubalkian
Implementation of Shift Cipher Encryption in Python 2.7
'''

import time

message = "pizza"
key = 3

def shiftEncrypt(m,k):
    s = ""
    v = ord("a")
    for x in m:
        s+=chr(v+(ord(x)+k-v)%26)
    return s

start = time.time()
print shiftEncrypt(message, key)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

slccd
--- 1.09672546387e-05 seconds ---

for input of message = 'pizza', key = 3.
'''