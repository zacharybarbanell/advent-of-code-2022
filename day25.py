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

linesT = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122""".split('\n')

lines = lines
    
q = deque()

s = set()

w='=-012'

def fr(s):
    o = 0
    for i in range(len(s)):
        c = s[-1-i]
        o += 5**i * (w.index(c)-2)
    return o

def to(n):
    s = ''
    for i in range(2*len(str(n)) + 5, -1, -1):
        if n > 5**i + sum(2 * 5**z for z in range(i)):
            s += '2'
            n -= 2*(5**i)
        elif n >= sum(2 * 5**z for z in range(i)):
            s += '1'
            n -= 5**i
        elif n <= -5**i - sum(2 * 5**z for z in range(i)):
            s += '='
            n += 2*(5**i)
        elif n <= -sum(2 * 5**z for z in range(i)):
            s += '-'
            n += 5**i
        else:
            s += '0'
    return s
    

for t in lines:
    o += fr(t)

print(o, to(o))







































