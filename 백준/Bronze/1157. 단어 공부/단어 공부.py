i = input().upper()
j = [i[y] for y in range(len(i))]
k = list(set(j))

ma_c = 0
ma = ""
ma_k = []

for x in range(0,len(k)):
    a =i.count(k[x])
    if a > ma_c:
        ma = k[x]
        ma_c = a
for x in range(0,len(k)):
    a =i.count(k[x])
    if a == ma_c:
        ma_k.append(k[x])

if len(ma_k) == 1:
    print(ma)
else:
    print("?")