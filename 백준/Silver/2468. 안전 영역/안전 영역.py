from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,Nk):
    
    q = deque()
    q.append((x,y))    
    while q:
        xf,yf = q.popleft()
        for i in range(4):
            nx = xf+dx[i]
            ny = yf+dy[i]
            if N > nx >= 0 and N > ny >= 0:
                if sf_map[ny][nx] > Nk and zero_map[ny][nx] != 1:
                    zero_map[ny][nx] = 1
                    q.append((nx,ny))
                
                
    


N = int(input())
sf_map = []
k = 0
for _ in range(N):
    aa = list(map(int,input().split()))
    sf_map.append(aa)
    k = max(aa) if k<max(aa)  else k
count = [0 for _ in range(k)]


for i in range(k):
    zero_map = [[0 for _ in range(N)]for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if sf_map[y][x] > i and zero_map[y][x] != 1:
                bfs(x,y,i)
                count[i] += 1

print(max(count))