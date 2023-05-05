t_1 = []

for _ in range(9) :
    t_1 += [list(map(int,input().split()))]
x = 0

for i in range(9):
    x = max(t_1[i]) if max(t_1[i]) > x else x

p_1,p_2 = 0,0
for j in range(9):
    for k in range(9):
        if t_1[j][k] == x:
            p_1,p_2 = j,k
print(x)
print(p_1+1,p_2+1)
