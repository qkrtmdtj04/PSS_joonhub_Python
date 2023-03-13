x = int(input())+1
a = ' '
s = '*'

for i in range(2,x+1):
  print(a * (i-2), end='')
  print(s * (x - i + 1), end='')
  print(s * (x - i ), end='')
  print()
