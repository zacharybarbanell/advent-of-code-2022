import string
import math
import os

import colorama
colorama.init(convert=True)

os.environ["AOC_SESSION"] = 'REMOVED'

import aocd

a = 0
b = 0
c = 0
o = 0
l = []

g= aocd.lines

def senic(x,y):
    a,b,c,d = x-1,x+1,y-1,y+1
    wa,wb,wc,wd = 0,0,0,0
    t = int(g[x][y])
    while a >= 0:
        v = int(g[a][y])
        wa += 1
        if v >= t:
            break
        a -= 1
    while b < len(g):
        v = int(g[b][y])
        wb += 1
        if v >= t:
            break
        b += 1
    while c >= 0:
        v = int(g[x][c])
        wc += 1
        if v >= t:
            break
        c -= 1
    while d < len(g[0]):
        v = int(g[x][d])
        wd += 1
        if v >= t:
            break
        d += 1
    return wa*wb*wc*wd
    


print(max((max(senic(x,y) for x in range(len(g))) for y in range(len(g[0])))))
