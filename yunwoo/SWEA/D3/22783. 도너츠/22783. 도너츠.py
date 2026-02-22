num = int(input())
for seq in range(1, num+1):
    n, m, k = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max_val = 0
    for i in range(0,n-k+1):
        for j in range(0,m-k+1):
            result = 0
            part = 0
            for x in range(i, i + k):
                result += sum(arr[x][j:j + k])
            for x in range(i+1, i+k-1):
                for y in range(j+1, j+k-1):
                    part += arr[x][y]
            if max_val <result-part:
                max_val = result-part

    print(f'#{seq} {max_val}')
