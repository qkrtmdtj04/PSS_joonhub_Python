a,b = map(int, input().split())
k = list(map(int, input().split()))

for i in range(len(k)):
    if b > k[i]:
        print(k[i], end=" ")
