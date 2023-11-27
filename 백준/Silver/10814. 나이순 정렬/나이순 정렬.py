a = int(input())

t = [ input().split() for _ in range(a)]

t.sort(key=lambda x:int(x[0]))

for i,x in t:
    print(f"{i} {x}")