T = int(input())
for tc in range(1,T+1):
    temp = list(map(int, input().split()))
    n = temp[0]
    charged = temp[1:]
    # dp로 풀어서 시간줄여보기
    # dp[i] = i번째 정거장까지의 최소 배터리 교체횟수
    dp = [float('inf')] * n
    dp[0] = -1

    for i in range(n-1):
        for j in range(1, charged[i]+1):
            if i+j < n:
                dp[i + j] = min(dp[i + j], dp[i] + 1)
            else:
                break
    print(f'#{tc} {dp[n-1]}')