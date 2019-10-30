'''
Author: Walker Kroubalkian
Implementation of Playfair Cipher Encryption in Python 2.7
'''

import time

message = "hikethefoothills"
key = "primrose"

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

def realMessage(m):
    s = ""
    l = len(m)
    i = 0
    while(i<l-1):
        if m[i]==m[i+1]:
            if(m[i]=="j"):
                s+="i"
            else:
                s+=m[i]
            s+="x"
            i+=1
        else:
            if((m[i]=="i" and m[i+1]=="j") or (m[i]=="j" and m[i+1]=="i")):
                s+="ix"
                i+=1
            else:
                if(m[i]=="j"):
                    s+="i"
                else:
                    s+=m[i]
                if(m[i+1]=="j"):
                    s+="i"
                else:
                    s+=m[i+1]
                i+=2
    if(i==l-1):
        if(m[i]=="j"):
            s+="ix"
        else:
            s+=m[i]
            s+="x"
    return s

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
    if(i1%5==i2%5):
        return g[(i1+5)%25]+g[(i2+5)%25]
    if(i1/5 == i2/5):
        v = 5*int(i1/5)
        return g[v+(i1+1)%5] + g[v+(i2+1)%5]
    r1 = i1/5
    r2 = i2/5
    c1 = i1%5
    c2 = i2%5
    return g[5*r1+c2] + g[5*r2+c1]
    

def playfairEncrypt(m,k):
    grid = constructGrid(k)
    trueMessage = realMessage(m)
    s = ""
    i = 0
    l = len(trueMessage)
    while(i<l):
        s+=solveTwo(trueMessage[i],trueMessage[i+1],grid)
        i+=2
    return s
    
start = time.time()
print playfairEncrypt(message, key)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

gmfcytfnizmugmqvvd
--- 3.79085540771e-05 seconds ---

for input of message = 'hikethefoothills', key = 'primrose'.
'''