N=int(input())
for _ in range(N):
  e,v= input().split()
  t=e.count(v)
  c=t*len(v)
  print(len(e)-c+t)