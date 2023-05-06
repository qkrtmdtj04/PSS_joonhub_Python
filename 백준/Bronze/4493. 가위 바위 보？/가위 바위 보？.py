a = int(input())

for _ in range(a):
    i = int(input())
    i_s_c = [0,0]
    for _ in range(i):
        k,r = input().split()
        if (k == 'P' and r == 'R') or (k == 'R' and r == 'S') or (k == 'S' and r == 'P'):
            i_s_c[0] += 1
        elif (r == 'P' and k == 'R') or (r == 'R' and k == 'S') or (r == 'S' and k == 'P'):
            i_s_c[1] += 1
    if i_s_c[0] == i_s_c[1]:
        print("TIE")
    elif i_s_c[0] < i_s_c[1]:
        print("Player 2")
    else:
        print("Player 1")