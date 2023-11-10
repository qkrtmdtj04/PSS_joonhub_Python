N = int(input())

page = [ [" " for _ in range(N)]for _ in range(N)]

def star(x,y,N):
    if N == 3:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                page[x+i][y+j] = "*"
        return
    
    new = N//3
    
    for xs in range(3):
            for ys in range(3):
                if xs == 1 and ys == 1:
                    continue
                star(x+xs*new,y+ys*new,new)
    
star(0,0,N)
for k in page:
    p = ""
    for u in k:
        p+=u
    print(p)