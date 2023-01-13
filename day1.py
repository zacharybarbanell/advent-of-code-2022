s = []
while True:
    i = input()
    if i == 'xxx':
        break
    s += [i]

a = 0
b = [0,0,0]
c = 0
for t in s:
    if t == '':
        b = [c] + b
        c = 0
    else:
        c += int(t)
        
b = sorted(b)
print(b[-1]+ b[-2] + b[-3])
