n,m = map(int,input().split())
t_1 = []
t_2 = []
for _ in range(n) :
    t_1 += [list(map(int,input().split()))]
for _ in range(n) :
    t_2 += [list(map(int,input().split()))]

for i in range(n):
    for j in range(m):
        print(t_1[i][j] + t_2[i][j],end=" ")
    print()