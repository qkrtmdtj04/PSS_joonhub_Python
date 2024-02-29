T = int(input())

for i in range(T):
    a, b, c = map(int,input().split())
    num = c // a + 1
    f = c % a
    if c % a == 0:
        num = c//a
        f = a
    print(f'{f*100+num}')