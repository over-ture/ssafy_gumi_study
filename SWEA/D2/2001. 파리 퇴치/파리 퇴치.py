num = int(input())
for seq in range(1, num + 1):
    number, ans = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(number)]

    max_val = 0
    for x in range(number - ans + 1):
        for y in range(number - ans + 1):
            sum_val = 0
            for i in range(ans):
                for j in range(ans):
                    sum_val += arr[x + i][y + j]
            if sum_val>max_val:
            	max_val = sum_val

    print(f'#{seq} {max_val}')
