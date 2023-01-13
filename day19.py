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

linesT = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.""".split('\n')

lines = lines

lines=lines[:3]

q = deque()

s = set()

o=1


def sdomcache(f):
    cachedresults = {}
    def rcheck(l, d):
        if l == tuple():
            return True
        return any(rcheck(l[1:],d[w]) for w in d if w >= l[0]) 

    def scheck(l, d):
        if l == tuple():
            return d
        if l[0] in d:
            return scheck(l[1:],d[l[0]])
        return None
    
    def fp(*args):
        if scheck(args, cachedresults) != None:
            return scheck(args, cachedresults)
        elif rcheck(args, cachedresults):
            return 0
        result = f(*args)
        z = cachedresults
        for a in args[:-1]:
            if a in z:
                z = z[a]
            else:
                z[a] = {}
                z = z[a]
        z[args[-1]] = result
        return result
    return fp



i = 0
for t in lines:
    i += 1
    _, a,b,c,d = t.split('costs')
    ore = (int(a.split(' ')[1]),0,0)
    cla = (int(b.split(' ')[1]),0,0)
    obs = (int(c.split(' ')[1]),int(c.split('and')[1].split(' ')[1]),0)
    geo = (int(d.split(' ')[1]),0,int(d.split('and')[1].split(' ')[1]))

    print(ore, cla, obs, geo)

    @cache
    def solve(t, orc, orp, clc, clp, obc, obp):
        if t == 0 or t == 1:
            return 0
        best = solve(t-1, orc + orp, orp, clc + clp, clp, obc + obp, obp)
        if orc >= ore[0] and orp < max(ore[0],cla[0],obs[0],geo[0]):
            best = max(best, solve(t-1, orc-ore[0] + orp, orp + 1, clc + clp, clp, obc + obp, obp))
        if orc >= cla[0] and clp < obs[1]:
            best = max(best, solve(t-1, orc-cla[0] + orp, orp , clc + clp, clp + 1, obc + obp, obp))
        if orc >= obs[0] and clc >= obs[1] and obp < geo[2]:
            best = max(best, solve(t-1, orc-obs[0] + orp, orp , clc-obs[1] + clp, clp, obc + obp, obp + 1))
        if orc >= geo[0] and obc >= geo[2]:
            best = max(best, solve(t-1, orc-geo[0] + orp, orp , clc + clp, clp, obc-geo[2] + obp, obp) + (t-1))
        return best
    o *= solve(32, 0, 1, 0, 0, 0, 0)        
    print(i,o)
    

    
print(o)






































