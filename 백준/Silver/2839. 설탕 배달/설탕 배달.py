import sys

a = int(sys.stdin.readline())

if a % 5 == 0: 
    print(a // 5)
else:
    count = 0
    while True:
        a -= 3
        count += 1
        if a % 5 == 0: 
            count += a // 5
            print(count)
            break
        elif a == 1 or a == 2: 
            print(-1)
            break
        elif a == 0:
            print(count)
            break