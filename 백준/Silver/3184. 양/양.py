from collections import deque

ddx = [-1,1,0,0]
ddy = [0,0,-1,1]

def bfs(x,y):
    t = {'v':0,'o':0}
   
    q = deque()
    q.append((x,y))    
    while q:
        xf,yf = q.popleft()
        for i in range(4):
            nx = xf+ddx[i]
            ny = yf+ddy[i]
            if M > nx >= 0 and N > ny >= 0:
                if sf_map[ny][nx] !='#' and zero_map[ny][nx] != 1:
                    zero_map[ny][nx] = 1
                    if sf_map[ny][nx] == 'v':
                        t['v'] += 1
                    if sf_map[ny][nx] == 'o':
                        t['o'] += 1
                    q.append((nx,ny))
    if t['o'] > t['v']:
        return 'do',t['o']
    else:
        return 'dv',t['v']                
    


N, M = map(int,input().split())
sf_map = [list(input()) for _ in range(N)]
zero_map = [[0 for _ in range(M)] for _ in range(N)]  #day확인용




dt = {'dv':0,'do':0}

for y in range(N):
    for x in range(M):
        if sf_map[y][x] == 'v' or 'o'and zero_map[y][x] != 1:
            dx,dy = bfs(x,y)
            dt[dx] += dy

print(dt['do'],dt['dv'])

