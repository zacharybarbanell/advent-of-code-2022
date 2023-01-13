import string
import math
import os

from collections import deque, defaultdict

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

linesT = """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..""".split('\n')

lines = lines
    
q = deque()

s = set()


j=0
for t in lines:
    for i in range(len(t)):
        if t[i] == '#':
            s.add( (i, j) )
    j += 1


D = ['U','D','L','R']

i = 0
while True:
    i += 1
    d = {}

    for e in s:


        
        ex, ey = e

        if not any(o in s for o in [(ex-1,ey-1),(ex,ey-1),(ex+1,ey-1),(ex-1,ey+1),(ex,ey+1),(ex+1,ey+1),(ex-1,ey),(ex+1,ey)]):
            d[e] = (0,0)
            continue


        for q in D:
            if q == 'U' and not any(o in s for o in [(ex-1,ey-1),(ex,ey-1),(ex+1,ey-1)]):
                d[e] = (0,-1)
                break
            if q == 'D' and not any(o in s for o in [(ex-1,ey+1),(ex,ey+1),(ex+1,ey+1)]):
                d[e] = (0,1)
                break
            if q == 'L' and not any(o in s for o in [(ex-1,ey-1),(ex-1,ey),(ex-1,ey+1)]):
                d[e] = (-1,0)
                break
            if q == 'R' and not any(o in s for o in [(ex+1,ey-1),(ex+1,ey),(ex+1,ey+1)]):
                d[e] = (1,0)
                break

        if e not in d:
            d[e] = (0,0)

    D = D[1:] + [D[0]]

    z = defaultdict(int)

    for e in s:
        ex, ey = e
        ox, oy = d[e]

        z[ex+ox,ey+oy] += 1

    sn = set()

    moved = False

    for e in s:
        ex, ey = e
        ox, oy = d[e]

        if z[ex+ox,ey+oy] == 1:
            sn.add( ( ex+ox,ey+oy) )
            if (ex+ox,ey+oy) != (ex, ey):
                moved = True
        else:
            sn.add( (ex, ey) )

    if not moved:
        print(i)
        break

            
    s = sn

    #for r in range(-5, 15):
        
        #print(''.join('.#'[(c, r) in s] for c in range(-5, 15)))
    #print()
    
    
    


#print( (1+max(e[0] for e in s) - min(e[0] for e in s))* (1+max(e[1] for e in s)- min(e[1] for e in s)) - len(s))






































