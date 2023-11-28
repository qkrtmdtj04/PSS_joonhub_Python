a = int(input())

t = [list(map(int,input().split())) for _ in range(a)]

t.sort(key=lambda x:(x[0],x[1]))

for i,x in t:
    print(f"{i} {x}")