import string
import math

s = []
while True:
    i = input()
    if i == 'xxx':
        break
    s += [i]

a = 0
b = 0
c = 0
o = 0
l = []
for t in s:
    q, w = t.split(',')
    a,b = q.split('-')
    
    c,d = w.split('-')
    if int(b) < int(c) or int(d) < int(a):
       o += 1
        

print(1000-o)
