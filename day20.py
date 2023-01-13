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

linesT = """1
2
-3
3
-2
0
4""".split('\n')

lines = lines

q = deque()

s = set()



class Node():
    def __init__(self, value, prev, nxt):
        self.val = value
        self.prv = prev
        self.nxt = nxt
    

startnode = Node(int(lines[0])* 811589153,None,None)
pnode = startnode

nodes = [startnode]

w = None
z = None

for t in lines[1:]:
    w = Node(int(t) ,pnode,None)
    if w.val == 0:
        z = w
    pnode.nxt = w
    pnode = w
    nodes.append(w)

w.nxt = startnode
startnode.prv = w

def swap(l, r):
    a,d = l.prv,r.nxt
    l.prv,l.nxt,r.prv,r.nxt = r,d,a,l
    a.nxt = r
    d.prv = l


for _ in range(1):
    for node in nodes:
        i = ((node.val + 2500) % (len(nodes) - 1)) - 2500
        
        while i > 0:
            swap(node,node.nxt)
            i -= 1
        while i < 0:
            swap(node.prv,node)
            i += 1

for i in range(1,3001):
    z = z.nxt
    if i % 1000 == 0:
        o += z.val

    
print(o)






































