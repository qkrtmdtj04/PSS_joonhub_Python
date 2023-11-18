N , K = map(int,input().split())
X = [int(input()) for _ in range(N)]

X.sort()

start = min(X)
end =  start + K
res = 0


while start <= end:
    mid = (start + end) //2
    up = 0
    for Xi in X:
        if Xi <= mid:
            up += (mid - Xi)
    if up <= K:
        res = max(res,mid)
        start = mid + 1
    else:
        end = mid -1

print(res)