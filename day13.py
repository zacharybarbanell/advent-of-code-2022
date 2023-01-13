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

data=aocd.lines

dataT = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""".split('\n')

q = deque()

def cmp(kk,ll):
    if type(kk) == type(0):
        k = kk
    else:
        k = [*kk]
    if type(ll) == type(0):
        l = ll
    else:
        l = [*ll]
    if k == l:
        return 0
    if type(k) == type(0):
        if type(l) == type(0):
            if k < l:
                return 1
            else:
                return -1
        return cmp([k],l)
    if type(l) == type(0):
        return cmp(k,[l])
    while len(k) > 0 and len(l) > 0:
        kf, lf = k.pop(0), l.pop(0)
        if (w := cmp(kf, lf)):
            return w
    if k == l:
        return 0
    if len(k) == 0:
        return 1
    return -1
        

for t in data:
    if t == '':
        continue
    else:
        l += [eval(t)]

l += [[[6]],[[2]]]

#print(l)

l = sorted(l, key=cmp_to_key(cmp))
l.reverse()

print((1+l.index([[2]]))*(1+l.index([[6]])))
