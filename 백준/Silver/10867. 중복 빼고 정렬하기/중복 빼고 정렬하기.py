t = int(input())
a = list(set(map(int,input().split())))
a.sort()
for i in a:
    print(i,end=" ")