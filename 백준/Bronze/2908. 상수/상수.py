p = input().split()

p[0],p[1] = int(p[0][::-1]),int(p[1][::-1])
print(max(p))