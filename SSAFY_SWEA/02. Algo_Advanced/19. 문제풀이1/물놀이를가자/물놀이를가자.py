import sys, os

if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)
# dp로 풀기(bfs 시간초과남;)

T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    dp = [[float('inf')] * (m+1) for _ in range(n+1)]
    # dp[i][j] = arr[i][j]에서 물까지의 최소 거리
    ans = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W': # 물이면 거리 0
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j]+1, dp[i][j-1]+1, dp[i+1][j]+1, dp[i][j+1]+1)
    for i in range(n):
        for j in range(m):
            if dp[i][j] != float('inf') and dp[i][j] != 0:
                ans += dp[i][j]
    print(ans)