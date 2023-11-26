import sys

N,M = map(int,sys.stdin.readline().split())

class_n = []
for _ in range(N):
    n, i = sys.stdin.readline().split()
    class_n.append((n,int(i)))


for _ in range(M):
    user = int(sys.stdin.readline())

    start = 0
    end = N
    res = ""
    while start <= end:
        mid = (start + end) // 2

        if class_n[mid][1] >= user:
            res = class_n[mid][0]
            end = mid -1
        else:
            start = mid +1
    print(res)
