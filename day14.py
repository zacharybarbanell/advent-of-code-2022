import string
import math
import os

from collections import deque

from functools import cmp_to_key

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

linesT = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".split('\n')

q = deque()

locs = {}
minh = 0

for t in lines:
    l = t.split(' -> ')
    px,py = None,None
    for loc in l:
        x, y = map(int,loc.split(','))
        if px != None:
            if px == x:
                for zy in range(min(y,py),max(y,py)+1):
                    locs[x,zy] = 1
            else:
                for zx in range(min(x,px),max(x,px)+1):
                    locs[zx,y] = 1
        px,py = x,y
        minh = max(minh, py)

for x in range(400 - minh, 600 + minh):
    locs[x, minh+2] = 1


t=True
while t:
    x, y = 500, 0
    while True:
        if (x, y+1) not in locs:
            y += 1
        elif (x-1, y+1) not in locs:
            x -= 1
            y += 1
        elif (x+1, y+1) not in locs:
            x += 1
            y += 1
        else:
            locs[x,y] = 1
            o += 1
            if x == 500 and y == 0:
                t = False
            break


print(o)








































