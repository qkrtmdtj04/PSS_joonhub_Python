
N = int(input())

for _ in range(N):
    end, cv = input().split()

    t = end.count(cv)
    if t > 0:
        c = t*len(cv)
        print(len(end)-c+t)
             
    else:
        print(len(end))
        break