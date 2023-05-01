p = input()
a = 'abcdefghijklmnopqrstuvwxyz'

for x in range(len(a)):
    if a[x] in p:
        print(p.index(a[x]),end=" ")
    else:
        print(-1,end=" ")