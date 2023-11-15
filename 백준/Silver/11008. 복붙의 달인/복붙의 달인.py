for _ in range(int(input())):
  e,v= input().split()
  t=e.count(v)
  c=t*len(v)
  print(len(e)-c+t)