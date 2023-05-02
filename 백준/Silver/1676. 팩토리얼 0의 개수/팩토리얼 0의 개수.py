
i = int(input())

c = 0
t = 0

while True:
	t += 1
	u = i//(5**t)
	if u == 0:
		break
	else:
		c += u
	
	
print(c)