import sys

N,M = map(int,sys.stdin.readline().split())

rubys = [int(sys.stdin.readline()) for _ in range(M)]

start = 1
end = max(rubys)
res = end

while start <= end:
    mid = (start + end) // 2

    sum_p = 0
    for ruby in rubys: 
        #여기에 보석 갯수 연산
        sum_p += ruby//mid
        if ruby%mid != 0:
            sum_p = sum_p+1

    if sum_p > N: # 보석 나눠준 갯수가 사람보다 많으면 크면 start값 올리기
        start = mid + 1
    else:
        end = mid -1

print(start)