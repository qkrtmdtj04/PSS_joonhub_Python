n = int(input())
t = [1,2,3]
for _ in range(n):
    k,j = map(int,input().split())
    t[k-1],t[j-1] = t[j-1],t[k-1]


print(t.index(1)+1)
