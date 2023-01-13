import string
import math
import os

from collections import deque

from functools import cmp_to_key, cache

import itertools

import colorama
colorama.init(convert=True)

os.environ["AOC_SESSION"] = 'REMOVED'

import aocd

a=0
b=0
c=0
l=[]
o=0

lines=aocd.lines

linesT = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>""".split('\n')

lines=lines

q = deque()

s = set()

z = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]


lx, hx = float('inf'),(-float('inf'))
ly, hy, lz, hz = lx, hx, lx, hx

for t in lines:
    u = eval('('+t+')')
    lx = min(lx, u[0])
    hx = max(hx, u[0])
    ly = min(ly, u[1])
    hy = max(hy, u[1])
    lz = min(lz, u[2])
    hz = max(hz, u[2])
    s.add(u)

lx -= 1
ly -= 1
lz -= 1
hx += 1
hy += 1
hz += 1


q.append((lx,ly,lz))
visited = {(lx,ly,lz)}

while q:
    w = q.popleft()
    for u in z:
        wp = (w[0] + u[0],w[1] + u[1],w[2] + u[2])
        
        if lx <= wp[0] <= hx and ly <= wp[1] <= hy and lz <= wp[2] <= hz:
            if wp not in s:
                
                if wp not in visited:
                    visited.add(wp)
                    q.append(wp)
            else:
                o += 1
    

    
print(o)






































