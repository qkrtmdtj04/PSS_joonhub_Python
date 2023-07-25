n = int(input())

for _ in range(n):
    n2 = int(input())
    m = list(map(int,input().split()))
    print(min(m) , max(m))