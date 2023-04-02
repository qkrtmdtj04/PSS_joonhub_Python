h,m=map(int,input().split())

m += h * 60 - 45
h = (m // 60) % 24
m %= 60
print(h, m)