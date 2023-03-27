from itertools import combinations

tall_list = [int(input()) for _ in range(9)]

for i in combinations(tall_list, 7):
  if sum(i)==100:
    for j in sorted(i):
      print(j)
    break