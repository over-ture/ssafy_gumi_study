import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)


T = int(input())
for tc in range(1,T+1):
    n,b = map(int, input().split())
    emp = list(map(int, input().split()))
    # 2차원 dp로풀어보기~~~~
    dp = [[False] * (sum(emp)+1) for _ in range(n+1)]
    # dp[i][h] = i번째 직원까지 고려했을 때 높이 h인 인간탑을 만들 수 있는가?(불린값임)
    dp[0][0] = True
    for i in range(1, n+1):
        for h in range(sum(emp)+1):
            if dp[i - 1][h] or dp[i - 1][h - emp[i-1]]:
                dp[i][h] = True
            # i번쨰 직원을 고려해서 높이 h가 되려면
            # 해당 직원이 없어도 높이가 h or 해당 직원 넣기 전까지의 높이가 h-emp[i-1] 여야 함
            # 둘 중 하나가 True면 됨
    # 최솟값 찾기
    ans = 0
    for h in range(b,sum(emp)+1):
        if dp[n][h]: # 처음으로 찾으면(최소임)
            ans = h-b
            break

    print(f'#{tc} {ans}')