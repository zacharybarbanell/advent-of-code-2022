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

linesT = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".split('\n')

q = deque()

m = {}

lbs = [[] for _ in range(4000000+1)]
ubs = [[] for _ in range(4000000+1)]

minx = 0

def md(p1, p2):
    return (abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]))

for t in lines:
    _, a,b,c,d = t.split('=')
    a = int(a.split(',')[0])
    b = int(b.split(':')[0])
    c = int(c.split(',')[0])
    d = int(d)
    
    m[a,b] = (c,d)

    
    r= md((a,b),(c,d))

    for y in range(b-r,b+r):
        if y < 0 or y > 4000000:
            continue
        dy = abs(y-b)
        fr = r-dy

        if fr >= 0:
            lbs[y] += [a - fr]
            ubs[y] += [a + fr]
    
    minx = max(minx, abs(a)+abs(b)+abs(c)+abs(d))

    
c=0
d = None


for y in range(4000000+1):
    lbs[y] = sorted(lbs[y])
    ubs[y] = sorted(ubs[y])
    if y % 100000 == 0:
        print(y)
    while True:
        if c == 0:
            if len(lbs[y]) == 0:
                break
            d = lbs[y].pop(0)
            c += 1
        elif (len(lbs[y]) > 0) and lbs[y][0] <= ubs[y][0]:
            o += lbs[y][0]-d
            d = lbs[y].pop(0)
            c += 1
        else:
            o += ubs[y][0]-d
            d = ubs[y].pop(0)
            c -= 1
            if c == 0 and d >= 0 and d <= 4000000:
                print(d+1,y)
    

print(o)








































