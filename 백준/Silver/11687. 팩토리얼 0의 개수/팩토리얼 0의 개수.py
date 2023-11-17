import sys

def count_trailing_zeros(n):
    count = 0
    power_of_5 = 5
    while n // power_of_5 > 0:
        count += n // power_of_5
        power_of_5 *= 5
    return count

def find_smallest_N_with_M_zeros(M):
    start = 0
    end = 5 * M  # 여유있게 큰 범위 설정

    result = -1  # 초기 결과를 -1로 설정

    while start <= end:
        mid = (start + end) // 2
        zeros = count_trailing_zeros(mid)

        if zeros == M:
            result = mid
            end = mid - 1  # 더 작은 N을 찾기 위해 범위를 왼쪽으로 좁힘
        elif zeros < M:
            start = mid + 1
        else:
            end = mid - 1

    return result

M = int(sys.stdin.readline())
result = find_smallest_N_with_M_zeros(M)


print(result)