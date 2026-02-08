num = int(input())
for seq in range(1, num+1):
    number = int(input())
    list_1 = list(map(int,input().split()))
    max_val = list_1[0]
    min_val = list_1[0]
    idx = 0
    idy = 0
    count = 0
    count_1 = 0
    for i in list_1:
        if max_val <= i:
            max_val = i
            idx = count
        count += 1
        if min_val > i:
            min_val = i
            idy = count_1
        count_1 += 1
    if (idx- idy)<0:
        result = idy-idx
    else:
        result = idx - idy
    print(f'#{seq} {result}')