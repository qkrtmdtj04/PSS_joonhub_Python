import sys

a = []
c = int(sys.stdin.readline())

for i in range(c):
    s = int(sys.stdin.readline())
    a.append(s)

a = sorted(a)

for i in a:
    print(i)
