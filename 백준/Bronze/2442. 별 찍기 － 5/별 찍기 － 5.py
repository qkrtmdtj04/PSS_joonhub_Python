x = int(input())+1
a = ' '
s = '*'

for i in range(2,x+1):
  print(a * (x - i), end='')
  print(s * (i - 1), end='')
  print(s * (i - 2), end='')
  print()