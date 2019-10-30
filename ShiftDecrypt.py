'''
Author: Walker Kroubalkian
Implementation of Shift Cipher Decryption with Key in Python 2.7
'''

import time

cipherText = "WIVHLVETPRERCPJZJTRESVLJVUFEFKYVIKPGVJFWTZGYVIJKFFSLKZKZJEFKLJLRCCPRJJZDGCVRJZKZJNZKYJYZWKTZGYVIJDREPFWKYVJVFKYVITZGYVIJNZCCRGGVRIYVIVZEKYVEVOKWVNDFEKY"
key = 17

def shiftDecrypt(c,k):
    c = c.lower()
    s = ""
    v = ord("a")
    for x in c:
        s+=chr(v+(ord(x)-k-v)%26)
    return s

start = time.time()
print shiftDecrypt(cipherText, key)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

frequencyanalysiscanbeusedonothertypesofcipherstoobutitisnotusuallyassimpleasitiswithshiftciphersmanyoftheseothercipherswillappearhereinthenextfewmonth
--- 4.98294830322e-05 seconds ---

for input of given cipher text and key of 17.
'''