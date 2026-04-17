<<<<<<< HEAD
n, k = map(int, input().split())
jim = []
max_w : 0
for i in range(n):
    w, v = map(int, input().split())
    jim.append((w,v))
jim.sort(key=lambda x : x[1])
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    weight = jim[i-1][0]
    value = jim[i-1][1]
    for now_w in range(1, k+1):
        if weight <= now_w: #i번째 물건을 now_w kg의 가방에 넣을 수 있을 때:
            dp[i][now_w] = max(dp[i-1][now_w], value + dp[i-1][now_w-weight])
            # 안 넣었을때 vs 가방에서 weight만큼을 빼고 해당 짐을 넣었을 때 중 최대
        else: #못넣으면
            dp[i][now_w] = dp[i-1][now_w] # 안넣었을때 무게

=======
n, k = map(int, input().split())
jim = []
max_w : 0
for i in range(n):
    w, v = map(int, input().split())
    jim.append((w,v))
jim.sort(key=lambda x : x[1])
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    weight = jim[i-1][0]
    value = jim[i-1][1]
    for now_w in range(1, k+1):
        if weight <= now_w: #i번째 물건을 now_w kg의 가방에 넣을 수 있을 때:
            dp[i][now_w] = max(dp[i-1][now_w], value + dp[i-1][now_w-weight])
            # 안 넣었을때 vs 가방에서 weight만큼을 빼고 해당 짐을 넣었을 때 중 최대
        else: #못넣으면
            dp[i][now_w] = dp[i-1][now_w] # 안넣었을때 무게

>>>>>>> f004f55cad382e72c8c19d5d4be06b3603ab15e3
print(dp[n][k])