i = [int(input()) for _ in range(10)]


k = list(set(i))
t = 0
p = 0
for ids in k:
    t1 = i.count(ids)
    if t < t1:
        t = t1
        p = ids
    
print(sum(i)//len(i))
print(p)