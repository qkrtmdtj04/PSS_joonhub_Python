o = [int(input()) for _ in range(5)]

for i in range(len(o)):
    if o[i] < 40:
        o[i] = 40

print(int(sum(o) / len(o)))