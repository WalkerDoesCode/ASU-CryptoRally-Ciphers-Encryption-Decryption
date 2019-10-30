'''
Author: Walker Kroubalkian
Implementation of Trifid Cipher Encryption in Python 2.7
'''

import time
from numpy import transpose

message = "costumeparty"
grid = 'xcrlk.wsyptdmjfiuaqnehzgvob'
period = 6

def getCoords(c,g):
    i = g.index(c)
    y = i/9
    x = (i%9)/3
    z = i%3
    return [x,y,z]

def getChar(coords, g):
    i = 9*coords[1]+3*coords[0]+coords[2]
    return g[i]

def trifidEncrypt(m,g,p):
    coords = []
    for x in m:
        coords.append(getCoords(x,g))
    rows = transpose(coords)
    l = len(rows[0])
    q = l/p
    s = []
    for i in range(q):
        for x in range(3):
            s.extend(rows[x][p*i:p*i+p])
    for x in range(3):
        s.extend(rows[x][p*q:])
    st = ""
    for i in range(0,len(s),3):
        st+=getChar(s[i:i+3],g)
    return st

start = time.time()
print trifidEncrypt(message, grid, period)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

enqjjmrrupya
--- 0.0001060962677 seconds ---

for input of message = 'costumeparty', grid = 'xcrlk.wsyptdmjfiuaqnehzgvob', period = 6.
'''