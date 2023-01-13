import string
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
for t in range(len(s)//3):
    y, u, i = s[3*t],s[3*t+1],s[3*t+2]
    for q in y:
        if (q in u) and (q in i):
            z = q
    
    c += (string.ascii_lowercase + string.ascii_uppercase).index(z)+1
        

print(c)
