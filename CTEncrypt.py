'''
Author: Walker Kroubalkian
Implementation of CT Cipher Encryption in Python 2.7
'''

import time

message = "cranberrieswithorangepeel"
key = "feast"

def getOrder(k):
    lk = len(k)
    orderCols = []
    for x in range(lk):
        orderCols.append(x)
    return sorted(orderCols, key=lambda x: k[x])

def ctEncrypt(m,k):
    columns = []
    lm = len(m)
    lk = len(k)
    for x in range(lk):
        column = []
        for i in range(x,lm,lk):
            column.append(m[i])
        columns.append(column)
    orderCols = getOrder(k)
    s = ""
    for x in orderCols:
        col = columns[x]
        for y in col:
            s+=y
    return s

start = time.time()
print ctEncrypt(message, key)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

ariaerrwrpcesoenitnebehgl
--- 2.69412994385e-05 seconds ---

for input of message = 'cranberrieswithorangepeel', key = 'feast'.
'''