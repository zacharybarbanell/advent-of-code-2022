import string
import math
import os

import colorama
colorama.init(convert=True)

os.environ["AOC_SESSION"] = 'REMOVED'

import aocd

w = 8
inventories = [[] for _ in range(w)]
operations = [None] * w
test = [None] * w
t_target = [None] * w
f_target = [None] * w

activity = [0] * w


g = aocd.lines

gt = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1


    """.split('\n')

tc = {}

for i in range(w):
    inventories[i] = [int(s[1:]) for s in g[7*i + 1].split(':')[1].split(',')]
    operations[i] = lambda o: (eval(g[7*i + 2].split('=')[1].replace('old',str(o))))
    tc[i] = int(g[7*i+3].split(' ')[-1])
    test[i] = lambda n: ((n % int(g[7*i+3].split(' ')[-1])) == 0)
    t_target[i] = int(g[7*i+4].split(' ')[-1])
    f_target[i] = int(g[7*i+5].split(' ')[-1])


gcd = 1
for x in range(w):
    gcd *= tc[x]

for u in range(10000):
    if u % 100 == 0:
        print(u)
    for i in range(w):
        while inventories[i]:
            x = inventories[i].pop()
            activity[i] += 1
            x = operations[i](x)
            if test[i](x):
                inventories[t_target[i]] += [x % gcd]
            else:
                inventories[f_target[i]] += [x % gcd]


print(sorted(activity))
