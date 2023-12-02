import sys

a, b = map(int,sys.stdin.readline().split())

ma,mi = max(a,b), min(a,b)

while True:
    t = ma % mi
    if t == 0:
        break
    mi,ma =  t,mi


for _ in range(mi):

    print(1, end='')
    

