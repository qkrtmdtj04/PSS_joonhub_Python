n = int(input())
s_s = []
for _ in range(n):
    j = list(map(int,input().split()))
    s = 0
    if j.count(j[0]) == 3:
        s += j[0]* 1000 + 10000
    elif j[0] == j[2]:
        s += j[0]*100+1000
    elif j[1] == j[2]:
        s += j[1]*100+1000
    elif j[0] == j[1]:
        s += j[1]*100+1000
    else:
        s += max(j)*100
    s_s.append(s)
print(max(s_s))