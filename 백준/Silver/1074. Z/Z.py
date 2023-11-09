N, r, c = map(int, input().split())

def zzz(N, r, c):

	if N == 0:
		return 0
        
	return 2*(r%2)+(c%2) + 4*zzz(N-1, r//2, c//2)

print(zzz(N, r, c))