a, b = map(int, input().split())
c = int(input())

b += a*60 + c
h,t = 0, 0

h += b // 60 
t += b % 60

if h > 23:
  h = h - 24

print(f"{h} {t}")