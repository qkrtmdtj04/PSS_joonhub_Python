N,M = map(int,input().split())
trees = list(map(int,input().split()))


start = 1
end =  sum(trees)


while start <= end:
    mid = (start + end) //2
    g = 0
    
    for Xi in trees:
        if Xi > mid:
            g += Xi - mid

    if g >= M:
        start = mid + 1
    else:
        
        end = mid -1


print(end)