k = ['a', 'e', 'i', 'o', 'u']
while True:
    i = input().lower()
    if i == "#":
        break
    c = 0
    for i_l in range(len(i)):
        for kk in k:
            if kk == i[i_l]:
                c += 1
    print(c)