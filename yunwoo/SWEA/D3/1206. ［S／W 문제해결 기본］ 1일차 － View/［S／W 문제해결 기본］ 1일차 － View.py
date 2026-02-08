for d in range(1, 11):
    num = int(input())
    a = list(map(int, input().split()))
    cnt = 0

    for i in range(2, num - 2):
        left_1 = a[i-2]
        left_2 = a[i-1]
        right_1 = a[i+1]
        right_2 = a[i+2]

        side_max = left_1
        if side_max < left_2:
            side_max = left_2
        if side_max < right_1:
            side_max = right_1
        if side_max < right_2:
            side_max = right_2
        if a[i] > side_max:
            cnt += a[i] - side_max

    print(f'#{d} {cnt}')
