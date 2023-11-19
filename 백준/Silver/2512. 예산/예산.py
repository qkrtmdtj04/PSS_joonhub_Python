N = int(input())
X = list(map(int,input().split()))
K = int(input())
X

start = 1
end =  max(X)
res = 0


while start <= end:
    mid = (start + end) //2
    up = 0
    
    for Xi in X:
        up += min(mid,Xi)


    if up <= K:

        res = mid
        start = mid + 1
    else:
        
        end = mid -1


print(res)