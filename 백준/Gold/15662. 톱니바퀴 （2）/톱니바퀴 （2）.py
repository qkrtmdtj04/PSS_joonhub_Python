n_lis = int(input())
gears = [list(map(int, input())) for _ in range(n_lis)]
k = int(input())

for _ in range(k):
    turns = [0] * n_lis   # 회전 종합 [0,0,0,0]
    gear, direction = map(int, input().split())
    turns[gear-1] = direction

    # 기어 확인
    for i in range(gear-1, 0, -1): # 기어 왼쪽 돌리는 기어 체크
        if gears[i][6] != gears[i-1][2]:
            turns[i-1] = -turns[i]
    for i in range(gear-1, n_lis-1):     # 기어 오른쪽 돌리는 기어 체크
        if gears[i][2] != gears[i+1][6]:
            turns[i+1] = -turns[i]
    # 기어 턴
    for i in range(n_lis):
        if turns[i] == 1:
            gears[i] = gears[i][-1:] + gears[i][:-1]
        elif turns[i] == -1:
            gears[i] = gears[i][1:] + gears[i][:1]


score = 0
for i in range(len(gears)):
    if gears[i][0] == 1:
        score += 1

print(score)
