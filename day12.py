import string
import math
import os

from collections import deque

import colorama
colorama.init(convert=True)

os.environ["AOC_SESSION"] = 'REMOVED'

import aocd

a=0
b=0
c=0
l=[]
o=0

g=aocd.lines

gt = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".split('\n')

h = {}

q = deque()

v  =set()

for y in (range(my:=len(g))):
    for x in (range(mx:=len(g[y]))):
        c = g[y][x]
        if c in 'SE':
            
            if c == 'S':
                h[x,y] = 0
                q.append(((x,y),0))
                v.add((x,y))
            else:
                h[x,y] = 25
                b = (x,y)
        else:
            h[x,y]=ord(c)-ord('a')
            if c == 'a':
                h[x,y] = 0
                q.append(((x,y),0))
                v.add((x,y))
        

a = ((1,0),(-1,0),(0,1),(0,-1))

while True:
    c, n = q.popleft()
    
    if c == b:
        print(n)
        break
    x, y = c
    #print(n, [x,y])
    for p in a:
        px, py = p
        px += x
        py += y
        if 0 <= px < mx and 0 <= py < my:
            if (px,py) not in v:
                if h[px,py]-h[x,y] <= 1:
                    q.append(((px,py),n+1))
                    v.add((px,py))


