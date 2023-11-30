from collections import deque

def blow(machines, R, C, total):
    #1: 오, 2:왼, 3:위, 4:아래
    for m in machines:
        md, mr, mc = m
        visited = diffuse(md, mr, mc)
        for i in range(R):
            for j in range(C):
                total[i][j] += visited[i][j]
    return total

def diffuse(md, mx, my):
    #x, y = mr, mc
    temp = [[0] * C for _ in range(R)]
    q = deque([])
    x, y = mx + dx[md], my + dy[md]
    temp[x][y] = 5
    q.append([x, y, 5])
    while q:
        x, y, t = q.popleft()
        if t < 1:
            return temp
        if md == 0:  # 오른쪽
            if upCh(x, y, 2):
                if rightCh(x - 1, y, md):
                    q.append([x - 1, y + 1, t - 1])
                    temp[x - 1][y + 1] = t - 1
            if rightCh(x, y, md):
                q.append([x, y + 1 , t - 1])
                temp[x][y + 1] = t - 1
            if downCh(x, y, 3):
                if rightCh(x + 1, y, md):
                    q.append([x + 1, y + 1, t - 1])
                    temp[x + 1][y + 1] = t - 1
        
        elif md == 1:  # 왼쪽
            if upCh(x, y, 2):
                if leftCh(x - 1, y, md):
                    q.append([x - 1, y - 1, t - 1])
                    temp[x - 1][y - 1] = t - 1
            if leftCh(x, y, md):
                q.append([x, y - 1, t - 1])
                temp[x][y - 1] = t - 1
            if downCh(x, y, 3):
                if leftCh(x + 1, y, md):
                    q.append([x + 1, y - 1, t - 1])
                    temp[x + 1][y - 1] = t - 1
        
        elif md == 2:
            if leftCh(x, y, 1):
                if upCh(x, y - 1, md):
                    q.append([x - 1, y - 1, t - 1])
                    temp[x - 1][y - 1] = t - 1
            if upCh(x, y, md):
                q.append([x - 1, y, t - 1])
                temp[x - 1][y] = t - 1
            if rightCh(x, y, 0):
                if upCh(x, y + 1, md):
                    q.append([x - 1, y + 1, t - 1])
                    temp[x - 1][y + 1] = t - 1
        
        elif md == 3:
            # q = downCheck(x, y, t, md, temp, q)
            if leftCh(x, y, 1):
                if downCh(x, y - 1, md):
                    q.append([x + 1, y - 1, t - 1])
                    temp[x + 1][y - 1] = t - 1
            if downCh(x, y, md):
                q.append([x + 1, y, t - 1])
                temp[x + 1][y] = t - 1
            if rightCh(x, y, 0):
                if downCh(x, y + 1, md):
                    q.append([x + 1, y + 1, t - 1])
                    temp[x + 1][y + 1] = t - 1
    return temp
 
def rightCh(x, y, i):
    if wall_ver[x][y] == 1:
        return False
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < R and 0 <= ny < C:
        #if not visited[nx][ny]:
        return True
    return False

def leftCh(x, y, i):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < R and 0 <= ny < C:
        #if not visited[nx][ny] and wall[nx][ny] == 1:
        if wall_ver[nx][ny] != 1:
            return True
    return False

def upCh(x, y, i):
    if wall_hori[x][y] == -1:
        return False
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < R and 0 <= ny < C:
        #if not visited[nx][ny]:
        return True
    return False

def downCh(x, y, i):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < R and 0 <= ny < C:
        #if not visited[nx][ny] and wall[nx][ny] == -1:
        if wall_hori[nx][ny] != -1:
            return True
    return False

def adjustment(total):
    temp = [[0] * C for _ in range(R)]

    for x in range(R):
        for y in range(C):
            if rightCh(x, y, 0):
                dif = total[x][y] - total[x][y + 1]
                if dif > 0:
                    ad = dif//4
                    if ad > 0:
                        temp[x][y] -= ad
                        temp[x][y + 1] += ad

            if leftCh(x, y, 1):
                dif = total[x][y] - total[x][y - 1]
                if dif > 0:
                    ad = dif // 4
                    if ad > 0:
                        temp[x][y] -= ad
                        temp[x][y - 1] += ad

            if upCh(x, y, 2):
                dif = total[x][y] - total[x-1][y]
                if dif > 0:
                    ad = dif // 4
                    if ad > 0:
                        temp[x][y] -= ad
                        temp[x - 1][y] += ad

            if downCh(x, y, 3):
                dif = total[x][y] - total[x+1][y]
                if dif > 0:
                    ad = dif // 4
                    if ad > 0:
                        temp[x][y] -= ad
                        temp[x + 1][y] += ad
    for x in range(R):
        for y in range(C):
            total[x][y] += temp[x][y]
    return total


# 가장 자리 온도 줄이기
def node_d(total):
    for j in range(C):
        if total[0][j] > 0:
            total[0][j] -= 1
    for j in range(C):
        if total[-1][j] > 0:
            total[R-1][j] -= 1

    for i in range(1, R-1):
        if total[i][0] > 0:
            total[i][0] -= 1
        if total[i][-1] > 0:
            total[i][-1] -= 1
    return total

if __name__=="__main__":
    chocolate = 0
    # 테스트 중단 조건 5번 위치가 K 이상
    # 1: 오, 2:왼, 3:위, 4:아래
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    R, C, K = map(int, input().split())
    arr = []
    fivesPos = []
    wall_hori = [[0] * C for i in range(R)]
    wall_ver = [[0] * C for i in range(R)]
    #wallVer = [[0] * C for i in range(R)]
    machines = []
    for r in range(R):
        data = list(map(int, input().split()))
        for c in range(C):
            if data[c] == 0:
                continue
            if data[c] == 5:
                fivesPos.append([r, c])
            # 온풍기들 위치
            else:
                machines.append([data[c]-1, r, c])
                data[c] = -1
        arr.append(data)

    W = int(input())
    for _ in range(W):
        x, y, d = map(int, input().split())
        if d == 0:
            wall_hori[x-1][y-1] = -1  # 위쪽
        else:
            wall_ver[x-1][y-1] = 1  # 오른쪽
    loopCnt = 0
    total = [[0] * C for _ in range(R)]
    while True:
        loopCnt += 1
        total = blow(machines, R, C, total)
        total = adjustment(total)
        total = node_d(total)
        chocolate += 1
        cnt = 0
        for [x, y] in fivesPos:
            if total[x][y] >= K:
                cnt += 1

        if cnt == len(fivesPos):
            print(loopCnt)
            break

        if loopCnt > 100:
            print(101)
            break
