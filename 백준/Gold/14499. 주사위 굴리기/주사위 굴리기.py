# 크기가 NxM인 지도
# 오른쪽(동쪽), 위쪽(북쪽)
# 주사위 전개도 2, 4/1/3, 5, 6
# 지도의 좌표 (r,c) r: 북쪽으로 부터 떨어진 갯수, c 서쪽으로 부터 떨어진 칸의 갯수

# 주사위 상태: 윗면 1, 동쪽 방향 3, 놓여져 있는 좌표 (x,y), 가장 처음에는 모든 면에 0

# 지도 각 칸에는 정수가 써있다 
# 주사위를 굴렸을때
# 1. 이동한 칸에 쓰여 있는 숫자가 0 일 경우
#    - 주사위 바닥면에 쓰여있는 수가 복사
# 2. 이동한 칸에 쓰여있는 수가 아닌 경우 
#    - 주사위 바닥면으로 복사, 이동했던 칸은 0으로
# 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시, 출력 NO.

# 입력
# N M x y K (지도 위치, 주사위 놓는 좌표, 명령 갯수)
# 지도 세팅
# 명령
# 명령마다 출력 
# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4


N,M,x,y,K = map(int,input().split())
map_list = [ list(map(int,input().split())) for _ in range(N)]
K_list = list(map(int,input().split()))

dice = [0,0,0,0,0,0] # 4/1/3, 5, 6, 2 => [1,5,6,2,4,3]  처음 윗면 1위치 0

def change():
    if map_list[x][y] == 0:
            map_list[x][y] = dice[2]
    else:
        dice[2] = map_list[x][y]
        map_list[x][y] = 0

for go in range(K):
    # 명령 시행
    # if문을 통해서 가장 먼저 x,y 이동확인 및 안되는 경우 검사
    if K_list[go] == 1 and y + 1 <= M-1: #y는 0~M-1
        y = y + 1
        dice[0],dice[4],dice[2],dice[5] = dice[4],dice[2],dice[5],dice[0] #주사위 동쪽으로 돌리기
        change()
        print(dice[0])

    
    elif K_list[go] == 2 and y - 1 >= 0:
        y = y - 1
        dice[4],dice[2],dice[5],dice[0] = dice[0],dice[4],dice[2],dice[5] #주사위 서쪽으로 돌리기
        change()
        print(dice[0])


    elif K_list[go] == 3 and x - 1 >= 0: #x는 0~N-1
        x = x - 1
        dice[0],dice[1],dice[2],dice[3] = dice[1],dice[2],dice[3],dice[0]
        change()
        print(dice[0])


    elif K_list[go] == 4 and x + 1 <= N-1:
        x = x + 1
        dice[1],dice[2],dice[3],dice[0] = dice[0],dice[1],dice[2],dice[3]
        change()
        print(dice[0])