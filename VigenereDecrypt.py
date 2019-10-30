'''
Author: Walker Kroubalkian
Implementation of Vigenere Cipher Decryption with Key in Python 2.7
'''

import time

cipherText = "FVPJSLXIDWSPUCFVGHYCYLVRQWWDGLXIDGCAFWWDGRNQCGKQBCQVOSOCOAZFBCVWSCXBWGCXRBRXCEJPWMSORFOSBQUWDLBVWUQGFURGDGBTFVPFSINFLHFVUGSGKRAGNGARJZZFU"
key = "jolson"

def vigenereDecrypt(c,k):
    c = c.lower()
    v = ord("a")
    i = 0
    l = len(k)
    s = ""
    for x in c:
        w = ord(k[i])-v
        s+=chr(v+(ord(x)-v-w)%26)
        i+=1
        i%=l
    return s

start = time.time()
print vigenereDecrypt(cipherText, key)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

whereyouseecloudsuponthehillsyousoonwillseecrowdsofdaffodilssokeeponlookingforabluebirdandlistningforhissongwheneveraprilshowerscomealong
--- 6.19888305664e-05 seconds ---

for input of given cipher text and key of "jolson".
'''