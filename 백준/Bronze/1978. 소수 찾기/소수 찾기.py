t = int(input())
s = list(map(int,input().split()))

ss = 0

for i in range(t):
    c = 0
    if s[i] > 1:
        for y in range(2, s[i]):
            if s[i] % y == 0:
                c += 1
        if c == 0:
            ss += 1
print(ss)