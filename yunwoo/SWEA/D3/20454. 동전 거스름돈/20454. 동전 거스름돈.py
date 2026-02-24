T = int(input())
for tc in range(1, T + 1):
    money = int(input())
    n = int(input())
    coins = list(map(int, input().split()))
 
    INF = 10**9
    dp = [INF] * (money + 1)
    dp[0] = 0
 
    for coin in coins:
        for m in range(coin, money + 1):
            dp[m] = min(dp[m], dp[m - coin] + 1)
 
    print(f'#{tc} {dp[money]}')