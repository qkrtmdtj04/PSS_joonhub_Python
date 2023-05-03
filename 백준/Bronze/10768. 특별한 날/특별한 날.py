i = int(input())
k = int(input())

if i > 2:
    print("After")
elif i < 2:
    print("Before")
else:
    if k > 18:
        print("After")
    elif k < 18:
        print("Before")
    else:
        print("Special")