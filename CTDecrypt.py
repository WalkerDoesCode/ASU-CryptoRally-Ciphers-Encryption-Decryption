'''
Author: Walker Kroubalkian
Implementation of CT Cipher Decryption in Python 2.7
'''

import time

cipherText = "UPILAIAPCHAKACUPDWEINACNEMNPREMETS"
key = "mayflower"

def getOrder(k):
    lk = len(k)
    orderCols = []
    for x in range(lk):
        orderCols.append(x)
    return sorted(orderCols, key=lambda x: k[x])

def invertOrder(orderCols):
    lk = len(orderCols)
    new = []
    for i in range(lk):
        new.append(orderCols.index(i))
    return new

def ctDecrypt(c,k):
    c = c.lower()
    orderCols = getOrder(k)
    inverted = invertOrder(orderCols)
    lc = len(c)
    lk = len(k)
    maxL = lc/lk
    colLengths = []
    for i in range(lk):
        colLengths.append(maxL)
    r = lc%lk
    if(r!=0):
        maxL+=1
    for i in range(r):
        colLengths[inverted[i]]+=1
    cols = []
    t = 0
    for x in colLengths:
        new = []
        for i in range(t,t+x):
            new.append(c[i])
        t+=x
        cols.append(new)
    orCols = []
    for x in inverted:
        orCols.append(cols[x])
    s = ""
    for i in range(maxL):
        for j in range(lk):
            if(len(orCols[j])>i):
                s+=orCols[j][i]
    return s

start = time.time()
print ctDecrypt(cipherText, key)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

pumpkinandpecanpiewithcaramelsauce
--- 4.6968460083e-05 seconds ---

for input of cipher text of 'UPILAIAPCHAKACUPDWEINACNEMNPREMETS', key = 'mayflower'.
'''