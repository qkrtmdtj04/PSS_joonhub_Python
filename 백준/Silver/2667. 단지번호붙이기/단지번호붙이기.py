from collections import deque
import sys
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    t = 1
    q = deque()
    set_map[y][x] = 0
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]

            if N > ny >= 0 and N > nx >= 0 :
                if set_map[ny][nx] == 1:
                    set_map[ny][nx] = 0
                    q.append((nx,ny))
                    t += 1
    return t



N =int(sys.stdin.readline())
set_map = [list(map(int,list(input()))) for _ in range(N)]



count = 0
p = []

for yy in range(N):
    for xx in range(N):
        if set_map[yy][xx] == 1:
            t =bfs(xx,yy)
            count = count + 1
            p.append(t)

p.sort()
print(count)
for pp in p:
    print(pp)