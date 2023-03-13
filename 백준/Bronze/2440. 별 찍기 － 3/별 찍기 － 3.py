x = int(input())+1
a = ' '
s = '*'

for i in range(2,x+1):
  print(s * (x - i + 1), end='')
  print()
