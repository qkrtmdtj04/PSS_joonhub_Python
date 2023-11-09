p1 = list(map(int,input().split()))
p2 = list(map(int,input().split()))

i = [0,0]
a = 0
for k in range(len(p1)):
    i[0] += p1[k]
    if i[0] > i[1]:
        a = 1
    i[1] += p2[k]
if a == 1:
    print("Yes")
else:
    print("No")