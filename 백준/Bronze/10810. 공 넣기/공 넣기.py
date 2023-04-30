a,b = map(int, input().split())
j = [0]*a


for i in range(b):
    x,y,z = map(int,input().split())
    j[x-1:y] = [z] * len(j[x-1:y])

for k in j:
    print(k,end=" ")
