import sys

input = sys.stdin.readline
n = int(input())
users = list(map(int, input().split()))
tmp = []
s = 1

for i in users:
	tmp.append(i)
	while len(tmp) != 0 and tmp[-1] == s: 
		tmp.pop()
		s = s + 1
	if len(tmp) > 1 and tmp[-1] > tmp[-2]:
		print("Sad")
		sys.exit()

if len(tmp) != 0:
	print("Sad")
else:
	print("Nice")