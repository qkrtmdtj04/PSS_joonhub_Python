a, b = map(int, input().split())
c = int(input())
x=b+c
print(f"{(a+(x//60))%24} {x%60}")