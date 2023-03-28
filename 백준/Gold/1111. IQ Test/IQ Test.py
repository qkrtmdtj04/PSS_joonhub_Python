n = int(input())
n_li = input().split()

for i in range(len(n_li)):
  n_li[i] = int(n_li[i])


if n == 1 or (n == 2 and n_li[0] != n_li[1]):
  print("A")
else:
  if n_li[0] - n_li[1] == 0:
    a = 0
  else:
    a = (n_li[1] - n_li[2]) // (n_li[0] - n_li[1])
    
  b = n_li[1] - n_li[0] * a

  for i in range(n - 1):
    expect = n_li[i] * a + b  # 다음 예측값
    if (n_li[i + 1] != expect):  # 예측값과 실제가 다르다면
      print('B')
      exit()
      
  print(n_li[-1] * a + b)