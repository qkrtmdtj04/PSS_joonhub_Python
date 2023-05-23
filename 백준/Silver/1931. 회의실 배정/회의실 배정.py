N = int(input())
k = []

for _ in range(N):
	a = list(map(int,input().split()))
	k.append([a[1],a[0]])


s = sorted(k)

t = [0, 0]
c = 0
end = 0
for i in range(len(s)):
	if s[i][1] >= t[0]:
		c += 1
		t = s[i]

print(c)