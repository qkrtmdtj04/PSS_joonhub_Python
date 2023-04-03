N = int(input())
dice_list = list(map(int,input().split()))

dice_list_1 = dice_list[:3][::-1] 
dice_list_2 = dice_list[3:]
dice_list_s = []

for y in range(len(dice_list_1)):
    if dice_list_1[y] > dice_list_2[y]:
        dice_list_s.append(dice_list_2[y])
    else:
        dice_list_s.append(dice_list_1[y])

c_1 = dice_list_s.count(dice_list_s[0])
dice_list_s = sorted(dice_list_s)
score = 0

c =  sum(dice_list)

if c_1 == 3:
    score += ((N*N)*5)* dice_list_s[0]
    print(score)
else:
    if N == 2:
        score += 8 * dice_list_s[0]
        score += 8 * dice_list_s[1]
        score += 4 * dice_list_s[2]
    elif N == 1:
        for i in range(len(dice_list)): # 0 1 2 3 4 5
            if c > sum(dice_list) - dice_list[i]:
                c = sum(dice_list) - dice_list[i]
        score += c

    else:
        # 가장 작은 수 만 존재하는 두면
        score += ((N*N) * 2) * dice_list_s[0]
        # 가장 높은 수 4개 합 고정 어떤 수가 와도
        score += dice_list_s[2] * 4
        # 가장 작은 수가 2번째로 많은 면 2면에 가장작은수 합
        score += (((N-2) * N) * 2 ) * dice_list_s[0]
        # 가장 작은 수가 2번째로 많은 면 2면에 가장작은수 합
        score += ((N*2-1) * 2) * dice_list_s[1]
        # 위에 주사위 가장 작은 수 합
        score += ((N-2)*(N-2)) * dice_list_s[0]
        # 위에 주사위 두번째 순서 수 합
        score += (6 + ((N-3)*4)) * dice_list_s[1]
    print(score)