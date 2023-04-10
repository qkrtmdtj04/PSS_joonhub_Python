s = int(input())

for i in range(s):
    a,b = map(int, input().split())
    print(f"Case #{i+1}: {a} + {b} = {a+b}")