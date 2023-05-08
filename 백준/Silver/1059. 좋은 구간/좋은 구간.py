i = int(input())
i_list = list(map(int,input().split()))
i_list = sorted(i_list)
n = int(input())

x = 0

if n in i_list:
    print(0)
else:
    min = 0
    max = 0
    for num in i_list:
        if num < n:     
            min = num
        elif num > n and max == 0:
            max = num
    max -= 1                   
    min += 1
    print((n-min)*(max-n+1) + (max-n))