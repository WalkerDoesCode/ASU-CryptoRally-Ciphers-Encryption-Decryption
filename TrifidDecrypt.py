'''
Author: Walker Kroubalkian
Implementation of Trifid Cipher Decryption in Python 2.7
'''

import time
from numpy import transpose

cipherText = "AQ.N.XJZVCUAEDHKXFZVYJRF"
grid = 'xcrlk.wsyptdmjfiuaqnehzgvob'
period = 4

def getCoords(c,g):
    i = g.index(c)
    y = i/9
    x = (i%9)/3
    z = i%3
    return [x,y,z]

def getChar(coords, g):
    i = 9*coords[1]+3*coords[0]+coords[2]
    return g[i]

def trifidDecrypt(c,g,p):
    c = c.lower()
    coords = ""
    for x in c:
        v = getCoords(x,g)
        for y in v:
            coords+=str(y)
    blockPeriod = 3*p
    lc = len(coords)
    i = 0
    st = ""
    while(i<=lc-blockPeriod):
        rows = []
        for x in range(3):
            row = []
            for y in range(p):
                row.append(int(coords[i+x*p+y]))
            rows.append(row)
        cols = transpose(rows)
        for col in cols:
            st+=getChar(col,g)
        i+=blockPeriod
    if(i!=lc):
        v = (lc-i)/3
        rows = []
        for x in range(3):
            row = coords[i+x*v:i+x*v+v]
            rows.append(row)
        cols = transpose(rows)
        for col in cols:
            st+=getChar(col,g)
    return st

start = time.time()
print trifidDecrypt(cipherText, grid, period)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

blackcatsandpointedhats.
--- 0.000282049179077 seconds ---

for input of cipherText = "AQ.N.XJZVCUAEDHKXFZVYJRF", grid = 'xcrlk.wsyptdmjfiuaqnehzgvob', period = 4.
'''