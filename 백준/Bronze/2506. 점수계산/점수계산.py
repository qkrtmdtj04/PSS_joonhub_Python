n = int(input())
k = list(map(int,input().split()))

c = 1
s_c = 0
for i in k:
    if i == 1:
        s_c += c
        c += 1
    else:
        c = 1
print(s_c)