import sys
from sys import stdin
from collections import deque

q = deque()

N = int(stdin.readline())
for _ in range(N):
    s = stdin.readline().split()
    
    if s[0] == 'push':
        q.append(int(s[1]))
    elif s[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif s[0] == 'size':
        print(len(q))
    elif s[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif s[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif s[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])