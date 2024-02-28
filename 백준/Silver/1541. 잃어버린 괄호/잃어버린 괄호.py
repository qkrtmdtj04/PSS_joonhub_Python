import sys

n = str(sys.stdin.readline())
m = n.split('-')

c = 0

x = sum(map(int, (m[0].split('+'))))
if n[0] == '-':
    c -= x
else:
    c += x

for x in m[1:]: 
    x = sum(map(int, (x.split('+'))))
    c -= x
print(c)