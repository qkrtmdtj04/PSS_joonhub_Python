import sys
def find_rank(ranking, new_score, P):
    left, right = 0, len(ranking)

    while left < right:
        mid = (left + right) // 2
        if ranking[mid] > new_score:
            left = mid + 1
        else:
            right = mid

    return left + 1


N, new_score, P = map(int, input().split())

if N > 0:
    ranking = list(map(int, input().split()))
else:
    ranking = []

if N == 0:
    print(1)
    sys.exit(0)
if N == P and new_score <= ranking[-1]:
    print(-1)
    sys.exit(0)

rank = find_rank(ranking, new_score, P)

if N == P and rank > P:
    print(-1)
else:
    print(rank)

