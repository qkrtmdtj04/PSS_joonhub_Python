chess = list(input().split())
chess_map = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}
chess_s= ["A","B","C","D","E","F","G","H"]

key = {"R":(1,0),"L":(-1,0),"B":(0,-1),"T":(0,1),"RT":(1,1),"LT":(-1,1),"RB":(1,-1),"LB":(-1,-1)}

#움직여야함   x 3 RRRLLLL    +1 +1 +1 -1 -
king = [chess_map[chess[0][0]],int(chess[0][1])]  #king A8 => king = [1,8] => king[0] = 1, king[1] = 8
r = [chess_map[chess[1][0]],int(chess[1][1])]

for i in range(int(chess[2])):
    move = str(input())
    x,y = key[move]   # RB => key["RB"] => 1-1
    if 9 > king[0] + x > 0 and  9 > king[1] + y > 0 :   #1,1
        king[0],king[1] = king[0] + x, king[1] + y
        
    if 9 > r[0] + x > 0 and  9 > r[1] + y > 0:
        if king[0] == r[0] and  king[1] == r[1]: 
            r[0],r[1] = r[0] + x, r[1] + y

    if king[0] == r[0] and  king[1] == r[1]:
        king[0],king[1] = king[0] - x, king[1] - y
    
king[0] = chess_s[king[0]-1] #0 ~ 7
r[0] = chess_s[r[0]-1]
print(f"{king[0]}{king[1]}")
print(f"{r[0]}{r[1]}")    
