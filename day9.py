import string
import math
import os

import colorama
colorama.init(convert=True)

os.environ["AOC_SESSION"] = 'REMOVED'

import aocd

tx,ty = ([0]*10,[0]*10)

v = {(0,0)}

w = {'D':(0,1),'U':(0,-1),'R':(1,0),'L':(-1,0)}

for t in aocd.lines:
    d, n = t.split(' ')
    n = int(n)
    dx, dy = w[d]
    for _ in range(n):
        tx[0] += dx
        ty[0] += dy
        for i in range(9):
            if tx[i] == tx[i+1] and abs(ty[i] - ty[i+1]) == 2:
                ty[i+1] = (ty[i] + ty[i+1])//2
            elif ty[i] == ty[i+1] and abs(tx[i] - tx[i+1]) == 2:
                tx[i+1] = (tx[i] + tx[i+1])//2
            elif tx[i] != tx[i+1] and ty[i] != ty[i+1] and (abs(tx[i]-tx[i+1]) + abs(ty[i]-ty[i+1]) > 2):
                tx[i+1] += (tx[i] - tx[i+1])//abs(tx[i]-tx[i+1])
                ty[i+1] += (ty[i] - ty[i+1])//abs(ty[i]-ty[i+1])
        v.add((tx[-1],ty[-1]))
        
    


print(len(v))
