import sys

def hanoi_top(k,point_top,suport_top,star_top):

    #k가 홀수일때는 처음 블럭을 목표지점으로
    #짝수일때는 보조 지점으로
    if k == 1:
        print(f"{star_top} {point_top}")
        return 
    
    hanoi_top(k-1,suport_top,point_top,star_top)
    print(f"{star_top} {point_top}")
    hanoi_top(k-1,point_top,star_top,suport_top)

i = int(sys.stdin.readline())
print(2**i-1)
if i <= 20:
    hanoi_top(i,3,2,1) 

