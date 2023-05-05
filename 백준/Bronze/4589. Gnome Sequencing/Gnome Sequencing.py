s = int(input())
print("Gnomes:")
for _ in range(s):
    n = list(map(int,input().split()))
    n_s = sorted(n)
    n_sr = sorted(n, reverse=True)
    if n == n_s or n == n_sr:
        print("Ordered")
    else:
        print("Unordered")