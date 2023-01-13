s = []
while True:
    i = input()
    if i == 'xxx':
        break
    s += [i]

a = 0
b = 0
c = 0
l = []
for t in s:
    x, y = t[0], t[2]
    a = '_XYZ'.index(y)
    b = '_ABC'.index(x)
    d = ((b - 2 + a - 1) % 3 )+ 1
    c += d + (((d - b + 1)%3)*3)
        

print(c)
