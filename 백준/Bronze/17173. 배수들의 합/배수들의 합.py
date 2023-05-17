N,m = map(int,input().split())
t = list(map(int,input().split()))

k_t = [False] * (N+1)


for i in t:
    for k_tr in range(i,len(k_t)):
        if k_tr % i  == 0:
            k_t[k_tr] = True

s = 0
for j in range(len(k_t)):
    if k_t[j]:
        s += j
print(s)
