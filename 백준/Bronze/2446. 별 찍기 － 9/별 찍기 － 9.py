i = int(input())
s ="*"
h =" "
for r in range(i):
  print(f'{h*r}{s*(i-(r+1))}{s*(i-r)}')

for r in range(2,i+1):
  print(f'{h*(i-r)}{s*r}{s*(r-1)}')
