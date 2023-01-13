import string
import math
import os

import colorama
colorama.init(convert=True)

os.environ["AOC_SESSION"] = 'REMOVED'

import aocd


ti = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".split('\n')

a = 0
b = 0
c = 0
o = 0
tree = {'~':0}

wd = '~'
for t in aocd.lines:
    if t[0] == '$':
        if t[2] == 'c':
            d = t[5:]
            if d == '/':
                wd = '~'
            elif d == '..':
                wd = '/'.join(wd.split('/')[:-1])
            else:
                wd += '/' + d
        else:
            tree[wd] = 0
        #print(wd)
    else:
        n = t.split(' ')[0]
        if n == 'dir':
            pass
        else:
            tree[wd] += int(n)

newtree = {}


for k in tree:
    newtree[k] = 0
    for w in tree:
        if k in w:
            newtree[k] += tree[w]


l = []

for v in newtree:
    l += [newtree[v]]

print(min(c for c in l if (newtree['~'] + 30000000 - c <= 70000000)))
