j = [int(input()) for i in range(10)]
k = {x%42 for x in j}

print(len(k))

