import string
import math
import os

os.environ["AOC_SESSION"] = 'REMOVED'

import aocd

a = 0
b = 0
c = 0
o = 0
l = []
stacks = [[] for _ in range(20)]
for t in aocd.lines[:8]:
    for x in range(9):
        c = t[4*x+1]
        if c != ' ':
            stacks[x] = [c] + stacks[x]

print(stacks)        

for t in aocd.lines[10:]:
    _, a, _, b, _, c = t.split(' ')
    a, b, c = int(a), int(b) - 1, int(c) - 1
    
    stacks[c] += stacks[b][0-a:]
    stacks[b] = stacks[b][:0-a]

print(''.join(s[-1] for s in stacks[:9]))
