t = int(input())

m = 2
while t != 1:
    if t%m==0:
        print(m)
        t //= m
    else:
        m+=1