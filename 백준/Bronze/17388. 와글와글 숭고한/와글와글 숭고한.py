k = list(map(int,input().split()))
if sum(k) >= 100:
    print("OK")
else:
    if k.index(min(k)) == 0:
        print("Soongsil")
    elif k.index(min(k)) == 1:
        print("Korea")
    else:
        print("Hanyang")