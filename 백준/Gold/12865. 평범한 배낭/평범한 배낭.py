N,K = map(int,input().split())


bag_list = [[0,0]]
DP = [[0] * (K+1) for _ in range(N+1)]

for _ in range(N):
    bag_list.append(list(map(int, input().split())))


for y in range(1,N+1):
    for x in range(1,K+1):
        w, v = bag_list[y]
        if x >= w:
            DP[y][x] = max(DP[y-1][x],v+ DP[y-1][x-w])
        else:
            DP[y][x] = DP[y-1][x]

print(DP[N][K])