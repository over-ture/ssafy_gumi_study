num = int(input())
def recur(n):
    dp = [0] * 31
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 5
    dp[4] = 11
    if n == 1:
        return 1
    else:
        for i in range(5, n + 1):
            dp[i] = dp[i-1]+dp[i-2]*2
    return dp[n]
for seq in range(1,num+1):
    result = 0
    n = int(input())
    n//=10
    result = recur(n)
    print(f'#{seq} {result}')
