j = [int(input()) for i in range(10)]
print(len({x%42 for x in j}))