import sys
sys.setrecursionlimit(10**6) 
S = input()
T = input()

def ab(t):
    if S==t:
        print(1)
        sys.exit()
    if len(t) == 0:
        return
    elif t[-1] == 'A':
        ab(t[:-1])
    elif t[-1] == 'B':
        ab(t[:-1][::-1])

ab(T)
print(0) 