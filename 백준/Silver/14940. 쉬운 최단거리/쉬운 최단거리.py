from collections import deque

def bfs(y,x):
    global ep,ma
    q = deque([(y,x)])
    ep[y][x] = 0
    while q:
        t = q.popleft()
        for i in range(4):
            ny = t[0] +bx[i]
            nx = t[1] +by[i]
            if 0<= ny < n and 0<=nx <m and ep[ny][nx] == 0:
                if ma[ny][nx]==1:
                    q.append((ny,nx))
                    ep[ny][nx] = 1 + ep[ t[0]][ t[1]]

                    
                    
                

n,m = map(int,input().split())

bx = [1,-1,0,0]
by = [0,0,1,-1]
ma = []
ep = []

for _ in range(n):
    ma.append(list(map(int,input().split())))
    ep.append([0 for _ in range(m)])




for y in range(n):
    for x in range(m): 
        if ma[y][x] ==2:
            bfs(y,x)
for y in range(n):
    for x in range(m): 
        if ma[y][x] ==1 and ep[y][x] ==0:
            ep[y][x] =-1

for y in range(n):
    for x in range(m):
        print(ep[y][x],end =' ')
    print()


