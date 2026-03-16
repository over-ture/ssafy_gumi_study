import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

# vis 배열에 특정 좌표에서 이동할 수 있는지를 기록(1이면 이동 가능)
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    vis = [0] * (n * n + 1)

    for r in range(n):
        for c in range(n):
            for d in range(4):
                nr, nc = r + dx[d], c + dy[d]
                if 0 <= nr < n and 0 <= nc < n:
                    if arr[nr][nc] == arr[r][c] + 1:
                        num = arr[r][c]
                        vis[num] = 1
                        break

    maximum = 0
    cnt = 0
    start = 0

    for i in range(1, n*n+1):
        if vis[i] == 1:
            cnt += 1
        else:
            if maximum < cnt:
                maximum = max(maximum, cnt)
                start = i - cnt
            cnt = 0

    print(f'#{tc} {start} {maximum + 1}')