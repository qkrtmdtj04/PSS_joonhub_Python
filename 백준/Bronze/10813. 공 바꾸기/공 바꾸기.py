a,b = map(int, input().split())
j = [i+1 for i in range(a)]


for i in range(b):
    x,z = map(int,input().split())
    j[x-1],j[z-1] = j[z-1],j[x-1]

for k in j:
    print(k,end=" ")
