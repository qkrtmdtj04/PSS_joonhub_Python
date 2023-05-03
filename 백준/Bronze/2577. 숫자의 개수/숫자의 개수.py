a = int(input())
b = int(input())
c = int(input())

k = str(a*b*c)
s_k = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(s_k)):
    for j in range(len(k)):
        if k[j] == str(i):
            s_k[i] += 1
            
for t in s_k:
    print(t)
