j = {int(input()) for i in range(28)}
f = {x + 1 for x in range(30)}

a = f.difference(j)
a = sorted(a)

for k in a:
    print(k,end=" ")
