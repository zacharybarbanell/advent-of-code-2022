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

linesT = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5""".split('\n')

lines = lines
    
q = deque()

s = set()

w = len(lines[0])
h = len(lines) - 2

c = min(x for x in range(w) if lines[0][x] == '.')
r = 0
f = 0

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def nxt(r, c, ff, s = False):
    global f
    #global lines
    rp, cp = r + d[ff][1], c + d[ff][0]
    rp %= h
    cp %= w
    if cp >= len(lines[rp]) or lines[rp][cp] == ' ':
        if cp == 0 and ff == 0:
            if not still and not s: print('a', r, c)
            cp = 99
            rp = 149 - rp
            if lines[rp][cp] != '#':f = 2
        elif cp == 100 and 100 <= rp <= 149 and ff == 0:
            if not still and not s: print('b', r, c)
            cp = 149
            rp = 149 - rp
            if lines[rp][cp] != '#':f = 2

        elif cp == 49 and 0 <= rp <= 49 and ff == 2:
            if not still and not s: print('c', r, c)
            cp = 0
            rp = 149 - rp
            if lines[rp][cp] != '#':f = 0
        elif cp == 149 and 100 <= rp <= 149 and ff == 2:
            if not still and not s: print('d', r, c)
            cp = 50
            rp = 149 - rp
            
            if lines[rp][cp] != '#':f = 0

        elif cp == 100 and 50 <= rp <= 99 and ff == 0:
            if not still and not s: print('e', r, c)
            cp = rp + 50
            rp = 49
            if lines[rp][cp] != '#':f = 3
        elif 100 <= cp <= 149 and rp == 50 and ff == 1:
            if not still and not s: print('f', r, c)
            rp = cp - 50
            cp = 99
            if lines[rp][cp] != '#':f = 2

        elif cp == 49 and 50 <= rp <= 99 and ff == 2:
            if not still and not s: print('g', r, c)
            cp = rp - 50
            rp = 100
            if lines[rp][cp] != '#':f = 1
        elif 0 <= cp <= 49 and rp == 99 and ff == 3:
            if not still and not s: print('h', r, c)
            rp = cp + 50
            cp = 50
            if lines[rp][cp] != '#':f = 0

        elif cp == 50 and 150 <= rp <= 199 and ff == 0:
            if not still and not s: print('i', r, c)
            cp = rp - 100
            rp = 149
            if lines[rp][cp] != '#':f = 3
        elif 50 <= cp <= 99 and rp == 150 and ff == 1:
            if not still and not s: print('j', r, c)
            rp = cp + 100
            cp = 49
            if lines[rp][cp] != '#':f = 2

        elif rp == 0 and ff == 1:
            if not still and not s: print('k', r, c)
            cp = cp + 100
            rp = 0
        elif rp == 199 and 100 <= cp <= 149 and ff == 3:
            if not still and not s: print('l', r, c)
            cp = cp - 100
            rp = 199

        elif rp == 199 and 50 <= cp <= 99 and ff == 3:
            if not still and not s: print('m', r, c)
            rp = 100 + cp
            cp = 0
            if lines[rp][cp] != '#':f = 0
        elif cp == 149 and 150 <= rp <= 199 and ff == 2:
            if not still and not s: print('n', r, c)
            cp = rp - 100
            rp = 0
            if lines[rp][cp] != '#':f = 1

        else:
            print(r,c, rp, cp)
            print(1/0)

        if not s:
            
            if lines[rp][cp] != '#':
                lines[r] = lines[r][:c] + '>v<^'[ff] + lines[r][c+1:]
                lines[rp] = lines[rp][:cp] + '>v<^'[f] + lines[rp][cp+1:]

    
    
    return rp, cp

still = False
a = ''    
for ch in lines[-1]:
    if ch in '0123456789':
        a += ch
    else:
        n = int(a)
        a = ''
        for _ in range(n):
            #lines[r] = lines[r][:c] + '>v<^'[f] + lines[r][c+1:]
            rp, cp = nxt(r,c,f)
            if lines[rp][cp] == '#':
                still = True
                pass
            else:
                still = False
                r, c = rp, cp
        #print(c,r,f)

        if ch == 'R':
            f = (f + 1) % 4
        else:
            f = (f - 1) % 4

n = int(a)     
for _ in range(n):
    rp, cp = nxt(r,c,f)
    if lines[rp][cp] == '#':
        pass
    else:
        r, c = rp, cp
#print(c,r,f)



for l in lines[:-2]:
    print(l)
print(r+1, c+1, f)
print(1000 * (r+1) + 4* (c+1) + f)






































