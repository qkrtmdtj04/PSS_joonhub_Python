# 토마토가 있으며 보관하루가 지나면 익은 토마토 옆에 익지 않은 토마토가 있으면 익는다
# 영향은 앞뒤오왼만 된다.
# 며칠이 지나면 다익게 되는지 최소 일 수
# 일부칸엔 없을 수 있다.

# 첫줄엔 M:가로 N:세로 2<M,N<1000
#정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
#무조건 bfs
from collections import deque
import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(one):
    day = 0
    q = deque()
    for y,x in one:
        q.append((day,x,y))
    d_day = 0
    while q:
        day,a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if to_b[ny][nx] == 0 :
                    to_b[ny][nx] = 1
                    #zero_b[ny][nx] = day + 1
                    d_day = day +1
                    q.append((day+1,nx,ny))
    return d_day




M, N = map(int,input().split())
to_b = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
#zero_b = [[0 for _ in range(M)] for _ in range(N)]  #day확인용



tt = [] #1있는 위치 담는 공간

#1있는 위치 y,x로 저장
for n in range(N):
    for m in range(M): 
        if to_b[n][m] == 1:
            tt.append([n,m])            
            
count = bfs(tt)

for n in range(N):
    for m in range(M):
        if to_b[n][m] == 0:
            print(-1)
            sys.exit(0)     
print(count)
