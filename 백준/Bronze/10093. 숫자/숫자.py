a,b = map(int,input().split())
min = a if a<b else b
max = a if a>b else b
i = [k for k in range(min+1,max)]


print(len(i))
for c in i:
    print(c,end=" ")