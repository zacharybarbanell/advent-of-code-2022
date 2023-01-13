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

adj = {}
r = {}

t=lines[0]

rocks = [
        ((0,0),(1,0),(2,0),(3,0)),
        ((1,0),(1,1),(1,2),(0,1),(2,1)),
        ((0,0),(1,0),(2,0),(2,1),(2,2)),
        ((0,0),(0,1),(0,2),(0,3)),
        ((0,0),(1,0),(0,1),(1,1))
    ]

def rock(x):
    return rocks[x%5]

n = 0

filled = {(x,0) for x in range(7)} 

def test(r, ox, oy):
    for w in r:
        wx, wy = w
        if (wx + ox, wy + oy) in filled or (wx + ox) not in range(7):
            return 1
    return 0

my = 0

ss = {}

i = 0

Dm = 0

q = 0

while i < 1000000000000:
    r = rock(i)
    i += 1
    
    ox = 2
    oy = my + 4
    while True:
        if n%len(t) == 0 and ss != None : 
            p = tuple(sorted(
                    sum(([(x,y) for x in range(7) if (x,my-y) in filled] for y in range(100)),start=[])
                ))
            #print(p)
            sd = (r, ox, oy-my, p)
            if sd in ss:
                
                oi, om = ss[sd]

                #print(i, oi)
                #print(ss, sd)
                rep = ((1000000000000 - i) // (i - oi)) - 5
                dm = rep * (my - om)
                i += rep * (i - oi)
                Dm += dm
                ss = None
                
            else:
                
                ss[sd] = i, my
            




        
        tox = ox + (1 if t[n%len(t)] == '>' else -1)
        n += 1
        if not test(r, tox, oy):
            ox = tox
        #print(tox,ox,oy)
        toy = oy - 1
        if not test(r, ox, toy):
            oy = toy
        else:
            for w in r:
                filled.add( (w[0] + ox, w[1] + oy) )
                #print((w[0] + ox, w[1] + oy),end='')
                my = max(my, w[1] + oy)
            #print()
            break

    
print(my + Dm)






































