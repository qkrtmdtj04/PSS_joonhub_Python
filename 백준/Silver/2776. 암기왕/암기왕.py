def ij_shch(sort_li,k):
    end = len(sort_li)-1
    start = 0
    
    while start <= end:
        mid = (start + end) // 2
        if sort_li[mid] == k:
            return 1
        elif sort_li[mid] < k:
            start = mid +  1
        else:
            end = mid - 1
    return 0
t_c = int(input())


for _ in range(t_c):
    len_1 = int(input())
    
    note_1 = list(map(int,input().split()))
    note_1.sort()

    len_2 = int(input())
    note_2 = list(map(int,input().split()))
    
    for in_2 in range(len(note_2)):
        print(ij_shch(note_1,note_2[in_2]))
        