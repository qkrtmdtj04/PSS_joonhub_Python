from collections import deque

def bfs(y,x):
    global ep,ma
    q = deque([(y,x)])
    ep[y][x] = 1
    while q:
        t = q.popleft()
        for i in range(4):
            ny = t[0] +bx[i]
            nx = t[1] +by[i]
            if 0<= ny < n and 0<=nx <m and ep[ny][nx] == 0:
                if ma[ny][nx]=='1':
                    q.append((ny,nx))
                    ep[ny][nx] = 1 + ep[ t[0]][ t[1]]

                    
                    
                

n,m = map(int,input().split())

bx = [1,-1,0,0]
by = [0,0,1,-1]
ma = []
ep = []

for _ in range(n):
    ma.append(input())
    ep.append([0 for _ in range(m)])


bfs(0,0)


print(ep[n-1][m-1])   


