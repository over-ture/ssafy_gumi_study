num = int(input())
for seq in range(1,num+1):
    n,k = map(int,input().split())
    dp = [[0]*(k+1) for _ in range(n+1)]
    arr = []
    for _ in range(n):
        v,c = map(int,input().split())
        arr.append((v,c))
    for i in range(1,n+1):
        w,v = arr[i-1]
        for j in range(1,k+1):
            if w>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)
    print(f'#{seq} {dp[n][k]}')