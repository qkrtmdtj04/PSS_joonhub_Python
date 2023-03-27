i, j = map(int, input().split())
to = [1, 3, 5, 7, 8, 10, 12]
ti = [4, 6, 9, 11]
y_li = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'] * (5 * i)
c = 0

for x in range(1,i):
  if x in to:
    c += 31
  elif x in ti:
    c += 30
  else:
    c += 28
c += j
print(y_li[c])