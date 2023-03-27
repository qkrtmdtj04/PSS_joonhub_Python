n = int(input())
a = []
for i in range(n):
  a.append(input().split())
  a[i][-1] = int(a[i][-1])
  a[i][-2] = int(a[i][-2])
  a[i][-3] = int(a[i][-3])


a.sort(key=lambda x:(x[-1], x[-2], x[-3]))

print(a[-1][0])
print(a[0][0])