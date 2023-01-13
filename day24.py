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

linesT = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#""".split('\n')

lines = lines
    
q = deque()

s = set()

w = len(lines[0]) - 2
h = len(lines) - 2

f = math.lcm(w, h)


y = -1
for t in lines:
    td = t[1:-1]
    for x in range(w):
        c = td[x]
        o = None
        if c == '<':
            o = (-1,0)
        elif c == '>':
            o = (1,0)
        elif c == '^':
            o = (0,-1)
        elif c == 'v':
            o = (0,1)
        if o != None:
            for z in range(f):
                n = ((x + o[0]*z) % w, (y + o[1]*z) % h)
                s.add( (z, n) )
    y += 1

q.append( (0, (0, -1)) )

g = [(-1,0),(1,0),(0,-1),(0,1),(0,0)]

v = set()

v.add( (0, (0, -1)) )

total = 0

while True:
    t, c = q.popleft()
    x, y = c
    if c == (w-1, h):
        total += t
        break
    for o in g:
        tp, xp, yp = t + 1, x + o[0], y + o[1]
        if (0 <= xp < w and 0 <= yp < h) or (xp == (w-1) and yp == h) or (xp == 0 and yp == -1):
            if (tp % f, (xp, yp)) not in v:
                if (tp % f, (xp, yp)) not in s:
                    q.append( (tp, (xp, yp)) )
                    v.add( (tp % f, (xp, yp)) )
q = deque()
q.append( (total, (w-1, h)) )
v = set()
v.add( (total, (w-1, h)) )

while True:
    t, c = q.popleft()
    x, y = c
    if c == (0, -1):
        total = t
        break
    for o in g:
        tp, xp, yp = t + 1, x + o[0], y + o[1]
        if (0 <= xp < w and 0 <= yp < h) or (xp == (w-1) and yp == h) or (xp == 0 and yp == -1):
            if (tp % f, (xp, yp)) not in v:
                if (tp % f, (xp, yp)) not in s:
                    q.append( (tp, (xp, yp)) )
                    v.add( (tp % f, (xp, yp)) )

q = deque()
q.append( (total, (0, -1)) )
v = set()
v.add( (total, (0, -1)) )

while True:
    t, c = q.popleft()
    x, y = c
    if c == (w-1, h):
        total = t
        break
    for o in g:
        tp, xp, yp = t + 1, x + o[0], y + o[1]
        if (0 <= xp < w and 0 <= yp < h) or (xp == (w-1) and yp == h) or (xp == 0 and yp == -1):
            if (tp % f, (xp, yp)) not in v:
                if (tp % f, (xp, yp)) not in s:
                    q.append( (tp, (xp, yp)) )
                    v.add( (tp % f, (xp, yp)) )

print(total)







































