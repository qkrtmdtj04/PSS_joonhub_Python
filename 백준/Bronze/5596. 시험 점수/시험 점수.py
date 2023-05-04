o = list(map(int,input().split()))
k = list(map(int,input().split()))
t =sum(k) if sum(k) > sum(o) else sum(o)
print(t)