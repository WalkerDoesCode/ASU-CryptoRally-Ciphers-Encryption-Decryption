'''
Author: Walker Kroubalkian
Implementation of Playfair Cipher Encryption in Python 2.7
'''

import time

message = "ILMILDRKRY"
key = "larkspur"

def constructGrid(k):
    grid = []
    for x in k:
        if x not in grid:
            if x=="j":
                if "i" not in grid:
                    grid.append("i")
            else:
                grid.append(x)
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    for a in alphabet:
        if a not in grid:
            grid.append(a)
    return grid

def solveTwo(a,b,g):
    try:
        i1 = g.index(a)
    except:
        raise Exception("The first character should appear in the grid.")
    try:
        i2 = g.index(b)
    except:
        raise Exception("The second character should appear in the grid.")
    if(i1==i2):
        raise Exception("The two characters should be different.")
    r1 = i1/5
    r2 = i2/5
    c1 = i1%5
    c2 = i2%5
    if(c1 == c2):
        return g[(i1-5)%25]+g[(i2-5)%25]
    if(r1 == r2):
        v = 5*r1
        return g[v+(i1-1)%5] + g[v+(i2-1)%5]
    return g[5*r1+c2] + g[5*r2+c1]
    

def playfairDecrypt(c,k):
    c = c.lower()
    grid = constructGrid(k)
    s = ""
    i = 0
    l = len(c)
    while(i<l):
        s+=solveTwo(c[i],c[i+1],grid)
        i+=2
    return s
    
start = time.time()
print playfairDecrypt(message, key)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

estesparkx
--- 3.09944152832e-05 seconds ---

for input of message = 'ILMILDRKRY', key = 'larkspur'.
'''