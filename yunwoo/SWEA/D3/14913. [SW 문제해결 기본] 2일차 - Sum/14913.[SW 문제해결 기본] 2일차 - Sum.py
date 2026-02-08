import sys
sys.stdin = open("test.txt")

for seq in range(1, 11):
    number = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_val = 0
    result_2 =0
    result_3 = 0
    for i in range(100):
        result = 0
        result_1 = 0
        for j in range(100):
            result +=arr[i][j]
            result_1 += arr[j][i]
            if i == j:
                result_2 += arr[i][j]
            if 99-i==j:
                result_3 +=arr[i][j]
        if result>=max_val:
            max_val = result
        if result_1 >= max_val:
            max_val = result_1
    if result_2 >= max_val:
        max_val = result_2
    if result_3 >= max_val:
        max_val = result_3
    print(f'#{seq} {max_val}')
