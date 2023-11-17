j = int(input())


a = [False,False] + [True]*(1004000)


for i in range(2,1004000):
    if a[i]:
        for p in range(2*i, 1004000, i):
            a[p] = False


while True:
    k = str(j) == str(j)[::-1]
    if a[j] and k:
        print(j)
        break
    j += 1