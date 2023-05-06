def such(s_li,k):
    end = len(s_li) - 1
    start = 0
    while start <= end:
        mid = (start+end)//2
        if s_li[mid] == k:
            return 1
        elif s_li[mid] < k:
            start = mid + 1
        else:
            end = mid - 1
    return 0



n_1_r = int(input())
n_1 = list(map(int, input().split()))
n_1.sort()
n_2_r = int(input())
n_2 = list(map(int, input().split()))

for i in n_2:
    print(such(n_1,i))