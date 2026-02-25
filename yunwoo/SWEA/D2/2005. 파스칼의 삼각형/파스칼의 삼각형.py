num = int(input())
for seq in range(1, num+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    for i in range(n):
        arr[i][0] = 1
    for i in range(1, n):
        for j in range(1, i+1):
            arr[i][j] = arr[i-1][j-1]+arr[i-1][j]
    print(f'#{seq}')
    for row in range(n):
        for col in range(n):
            if arr[row][col] != 0:
                print(arr[row][col], end=" ")
        print()