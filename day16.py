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

linesT = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".split('\n')

q = deque()

adj = {}
r = {}

for t in lines:
    n = t.split(' ')[1]
    z = t.split('valve')[1][1:]
    if z[0] == ' ':
        z = z[1:]
    adj[n] = tuple(z.split(', '))
    w = int(t.split(';')[0].split('=')[1])
    if w > 0:
        r[n] = w

@cache
def dist(a, b):
    q = deque()
    q.append((a, 0))
    visited = {a}
    while True:
        c, n=q.popleft()
        if c == b:
            return n
        for w in adj[c]:
            if w not in visited:
                visited.add(w)
                q.append((w,n+1))

@cache
def solve(loc, enabled, t):
    if t == 0:
        return 0
    else:
        best = sum(r[x] for x in enabled) * t
        for o in r:
            if o not in enabled:
                d = dist(loc, o)
                if d < t:
                    ac = sum(r[x] for x in enabled) * (d+1) + solve(o, tuple(sorted(enabled + (o,))), t - (d+1))
                    best = max(best, ac)

        return best

def powerset(s):
    if s == set():
        return [set()]
    r = next(iter(s))
    l = []
    for u in powerset(s-{r}):
        l += [{r}|u,u]
    return l


u = 0

@cache
def solve2(loc, enabled, t, sub):
    if t == 0:
        return 0
    else:
        best = sum(r[x] for x in enabled) * t
        for o in r:
            if (o not in enabled) and (o in sub):
                d = dist(loc, o)
                if d < t:
                    ac = sum(r[x] for x in enabled) * (d+1) + solve2(o, tuple(sorted(enabled + (o,))), t - (d+1), sub)
                    best = max(best, ac)
        if not enabled:
            global u
            u += 1
            if u % 100 == 0:
                print(u)
        return best


    
print(solve('AA',tuple(),30))

print(
    max(
        solve2('AA',tuple(),26,tuple(sorted(tuple(s)))) + \
        solve2('AA',tuple(),26,tuple(sorted(tuple(set(r)-s)))) \
        for s in powerset(set(r))
        )
    )







































