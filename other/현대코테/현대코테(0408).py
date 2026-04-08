import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def dist(curr, nxt):
    nx, ny = (curr-1)//w, (curr-1)%w
    tx, ty = (nxt-1)//w, (nxt-1)%w
    dist = abs(nx-tx) + abs(ny-ty)

    return dist

T = int(input())
for tc in range(1,T+1):
    w, h = map(int, input().split())
    arr = []
    for i in range(h):
        temp = [x + w * i for x in range(1, w+1)]
        arr.append(temp)
    blocks = list(map(int, input().split()))
    n = len(blocks)
    dists = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dists[i][j] = dist(blocks[i], blocks[j])
    dp = [[float('inf')] * n for _ in range(1<<n)]

    for i in range(n):
        # (0, 0) 좌표와 i번째 블록의 좌표 사이의 거리 계산
        dist_from_start = dist(1, blocks[i])

        # i번 블록만 방문한 상태(1 << i)에서 현재 위치가 i일 때의 초기값
        dp[1 << i][i] = dist_from_start

    for i in range(1, 1<<n):
        for curr in range(n): # 특정 정점들을 경유하고 난 뒤의 현재 위치
            if (not i & (1<<curr)) or dp[i][curr] == float('inf'): # 현재 지점을 경유하지 않거나 아직 기록되지 않았다면
                continue # 패스

            for nxt in range(n):
                if i & (1<<nxt):
                    continue

                nxt_vis = i | (1 << nxt)

                dp[nxt_vis][nxt] = min(dp[i][curr] + dists[curr][nxt], dp[nxt_vis][nxt])

    ans_idx = (1<<n) - 1
    ans = min(dp[ans_idx])
    print(f'#{tc} {ans}')