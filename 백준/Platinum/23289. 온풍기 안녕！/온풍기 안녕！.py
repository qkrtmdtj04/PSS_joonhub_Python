#온풍기 바람 보내기 함수 (벽고려)

def pen(index,row,def_point,zero_map,wall=[]):

    numbers = [5,4,3,2,1]
    for r in range(5): #가운데 줄
        if row > def_point[1]+r and [def_point[0],def_point[1]+r] not in wall:
            zero_map[def_point[0]][def_point[1]+r] = zero_map[def_point[0]][def_point[1]+r] + numbers[r]    
            continue
    r_d_go = 0
    for r_d in range(def_point[0]+1, def_point[0]+5): 
        r_d_go = r_d_go + 1
        # 4 5 6 7 8 
        if r_d >= index:  # 4 5 6
            break
        for r in range(r_d_go,5):
            if row > def_point[1]+ r and [r_d,def_point[1]+r] not in wall:
                zero_map[r_d][def_point[1] + r] = zero_map[r_d][def_point[1] + r] + numbers[r]
    r_u_go = 0   
    for r_u in range(def_point[0]-1, def_point[0]-5,-1): 
        r_u_go = r_u_go + 1
        if r_u < 0:  # 4 5 6
            break
        for r in range(r_u_go,5):
            if row > def_point[1]+r and [r_u,def_point[1]+r] not in wall:
                zero_map[r_u][def_point[1]+r] = zero_map[r_u][def_point[1]+r] + numbers[r]
    
    return zero_map


# 입력창 실행 

R, C, K = map(int,input().split())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
fives = []
rxc_map = []
rxc_map_zero = []
hot_def_point = []
for r in range(R):
    c_map = list(map(int,input().split()))
    for c in range(len(c_map)):
        if c_map[c] == 5:
            fives.append([r, c])
    rest_list = list(filter(lambda x: c_map[x] > 0 and c_map[x] != 5 , range(len(c_map))))
    hot_def_point.append(rest_list)
    rxc_map.append(c_map)
    rxc_map_zero.append([0 for _ in range(C)])

wall_len = int(input())
wall_x = []
wall_y = []
wallHori = [[0] * C for i in range(R)]
wallVer = [[0] * C for i in range(R)]
for _ in range(wall_len):
    wall_x_map = list(map(int,input().split()))
    if wall_x_map[2] == 0:
        wall_x.append(wall_x_map[:2])
        wallVer[wall_x_map[0]-1][wall_x_map[1]-1] = 1  # 오른쪽
    elif  wall_x_map[2] == 1:
        wall_y.append(wall_x_map[:2])
        wallHori[wall_x_map[0]-1][wall_x_map[1]-1] = -1  # 위쪽


#온풍기 위치 변환 함수

def hot_pen(map,point):  #def_point (x,y) x랑 y 반대로 쓴거 같은데
    global rxc_map_zero
    if map[point[0]][point[1]] == 1: #오른쪽 바람
        rxc_map_zero = pen(R,C,point,rxc_map_zero,wall_y)

    elif map[point[0]][point[1]] == 2: #왼쪽 바람
        wall_y_2 = []
        rxc_map_zero = [rxc_map_zero[i][::-1] for i in range(len(rxc_map_zero))] #뒤집기
        point[1] = -(point[1] - C)
        for wall_y_len in range(len(wall_y)):
            wall_y_2.append([wall_y[wall_y_len][0],-(wall_y[wall_y_len][1] - C)])
        rxc_map_zero = pen(R,C,point,rxc_map_zero,wall_y_2)
        rxc_map_zero = [rxc_map_zero[i][::-1] for i in range(len(rxc_map_zero))] #복구
      
    
    elif map[point[0]][point[1]] == 3: #아래쪽 바람
        wall_x_3 = []
        rxc_map_zero = [list(k[::-1]) for k in zip(*rxc_map_zero)]
        point[0],point[1] = point[1],-(point[0] - C)-1
        for wall_x_len in range(len(wall_x)):
            wall_x_3.append([wall_x[wall_x_len][1]-1,-(wall_x[wall_x_len][0] - C)])
        rxc_map_zero = pen(C,R,point,rxc_map_zero,wall_x_3)
        rxc_map_zero = [list(k) for k in zip(*rxc_map_zero)][::-1]
        


    elif map[point[0]][point[1]] == 4: #위쪽 바람
        wall_x_4 = []
        rxc_map_zero = [list(k) for k in zip(*rxc_map_zero)][::-1]
        point[0],point[1] = -(point[1] - R),point[0]+1
        for wall_x_len in range(len(wall_x)):
            wall_x_4.append([-(wall_x[wall_x_len][1] - R)+1, wall_x[wall_x_len][0]-1])
        rxc_map_zero = pen(C,R,point,rxc_map_zero,wall_x_4)
        rxc_map_zero = [list(k[::-1]) for k in zip(*rxc_map_zero)]
 
def rightCh(x, y, i):
    if wallVer[x][y] == 1:
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
        if wallVer[nx][ny] != 1:
            return True
    return False

def upCh(x, y, i):
    if wallHori[x][y] == -1:
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
        if wallHori[nx][ny] != -1:
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
            #visited[x][y] = 1
    return temp


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




# 명령어 실행 

chocolate = 0

loopCnt = 0
total = [[0] * C for _ in range(R)]
while True:
    loopCnt += 1
    for i in range(len(hot_def_point)):
        if len(hot_def_point[i]) != 0:
            for j in range(len(hot_def_point[i])):
                hot_pen(rxc_map,[i,hot_def_point[i][j]])
            
    a = adjustment(rxc_map_zero)
    for x in range(R):
        for y in range(C):
            a[x][y] += rxc_map_zero[x][y]
        
    total = node_d(a)
    chocolate += 1
    cnt = 0
    for [x, y] in fives:
        if total[x][y] >= K:
            cnt += 1

    if cnt == len(fives):
        print(loopCnt)
        break

    if loopCnt > 100:
        print(101)
        break