import sys

m = int(sys.stdin.readline())
s = set()

for _ in range(m):
    q = sys.stdin.readline().strip().split()
    
    if len(q) == 1:
        if q[0] == "all":
            s = set([i for i in range(1, 21)])
        else:
            s = set()
    
    else:
        func, x = q[0], q[1]
        x = int(x)

        if func == "add":
            s.add(x)
        elif func == "remove":
            s.discard(x)
        elif func == "check":
            d = 1 if x in s else 0
            print(d)
        elif func == "toggle":
            if x in s:
                s.discard(x)
            else:
                s.add(x)