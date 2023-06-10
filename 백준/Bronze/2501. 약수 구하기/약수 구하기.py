p,k = map(int, input().split())
c = []

for i in range(1,p+1):
    if p%i==0:
        c.append(i)

if len(c) < k:
    print(0)
else:
    print(c[k-1])
