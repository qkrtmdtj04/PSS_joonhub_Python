p = int(input())
a = list(map(int, input().split()))
m = max(a)
for i in range(p):
    a[i] = a[i] / m * 100

print(sum(a)/p)

