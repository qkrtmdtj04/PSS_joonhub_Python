a = int(input())
s,t = 0,1

for c in range(a):
  s,t = t, s + t

print(s)