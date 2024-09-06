from collections import deque



m,s = map(int,input().split())
m2 = {}

counts = [0] * 101 
visited = [False] * 101  
for i in range(m+s):
    x,y = map(int,input().split())
    m2[x] = y


d = deque([(1,0)])

while d:
    t = d.popleft()
    a = t[0]
    r = t[1]
    if a == 100:
        print(r)
        break

    for i in range(1,7):
        if a+i < 100 and not visited[a+i]:
            if a+i in m2:
                d.append((min(100, m2[a+i]), r+1))
            else: d.append((min(100, a+i), r+1))
            visited[a+i] = True 
        elif a+i >= 100:
            d.append((100, r+1))
            visited[100] = True
        