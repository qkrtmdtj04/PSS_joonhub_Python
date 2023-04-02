a = input().split()
max_a = [1,1,2,2,2,8]

for i in range(len(max_a)):
  print(max_a[i] - int(a[i]), end=" ")