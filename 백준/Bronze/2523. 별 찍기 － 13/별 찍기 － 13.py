a = int(input())
s = "*"
h = " "


for i in range(1,a+1):
  print(f"{s*i}")
for j in range(a-1,0,-1):
  print(f"{s*j}")
