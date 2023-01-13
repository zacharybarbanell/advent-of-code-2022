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

linesT = """TODO""".split('\n')

lines = lines

q = deque()

s = set()

for t in lines:
    a, b = t.split(':')
    #if a == 'root':
    #    root = b.split(' ')[0], b.split(' ')[1]
    if s == 'humn':
        pass
    s.add((a +'='+ b))

for u in s:
    print(u)

while s:
    #print(len(s))
    w = {z for z in s}
    for u in w:
        try:
            exec(u)
            s.remove(u)
        except Exception as e:
            pass
        

    
print(root)






































