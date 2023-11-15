for _ in range(int(input())):
  e,v= input().split()
  t=e.count(v)
  print(len(e)-t*len(v)+t)