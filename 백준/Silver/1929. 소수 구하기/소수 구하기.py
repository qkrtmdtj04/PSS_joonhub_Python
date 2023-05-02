m,n = map(int,input().split())


a = [False,False] + [True]*(n-1)


for i in range(2,n+1):
    if a[i]:
        for j in range(2*i, n+1, i):
            a[j] = False
            
for j in range(m,n+1):
    if a[j]:
        print(j)