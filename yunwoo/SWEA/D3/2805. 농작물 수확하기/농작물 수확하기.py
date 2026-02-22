num = int(input())
for seq in range(1,num+1):
    n = int(input())
    arr = [list(map(int,input())) for _ in range(n)]
    total = 0
    x = int(n/2)
    i = 0
    for i in range(n):
        if i <= x:
            total += sum(arr[i][x - i: x + i + 1])
        else:
            total += sum(arr[i][i - x: n - (i - x)])
    print(f'#{seq} {total}')
