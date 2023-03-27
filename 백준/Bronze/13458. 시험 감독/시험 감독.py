n = int(input())
a_i = input().split()
b,c = map(int,input().split())

s = 0

for x in range(len(a_i)):
  a_i[x] = int(a_i[x])
  
for i in range(len(a_i)):
  if a_i[i] - b < 0:
    a_i[i] = 0
    s += 1
  else:
    a_i[i] -= b
    s += 1
  if a_i[i] % c != 0:
    s += (a_i[i] // c) + 1
  else:
    s += (a_i[i] // c)
  
print(s)
