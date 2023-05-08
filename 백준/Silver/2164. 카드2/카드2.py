import sys
from collections import deque
i = int(sys.stdin.readline())
icard = deque([k for k in range(1,i+1)])

while len(icard) != 1:
    icard.popleft()
    num = icard.popleft()
    icard.append(num)


print(icard[0])