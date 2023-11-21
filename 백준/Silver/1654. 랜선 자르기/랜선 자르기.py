import sys

K, N = map(int,sys.stdin.readline().split())
lan_cables = [int(sys.stdin.readline()) for _ in range(K)]

cut = 0
start = 1
end = max(lan_cables)+1

while start <= end:
    cut_c = 0
    mid = (start+end)//2

    for lan_cable in lan_cables:
        cut_c += lan_cable//mid
    
        
    if cut_c < N:
        end = mid-1
    else:
        cut = max(cut, mid)
        start = mid +1

print(cut)