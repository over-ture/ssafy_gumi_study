import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

dxs, dys = [-1, 1, 1, -1], [1, 1, -1, -1] # 대각선 4방향


def in_range(x,y):
    return 0 <= x < N and 0 <= y < N

def dfs(x, y, d, cnt):
    global sx, sy, ans

    # 도착하면
    if d == 3 and x == sx and y == sy:
        ans = max(ans, cnt) # 기존 최댓값과 비교
        return

    # 아니면
    for i in range(2):
        nd = d + i
        if nd > 3:
            break # 4부터는 사각형이 깨짐

        nx, ny = x + dxs[nd], y + dys[nd]
        # 처음으로 돌아오기
        if nd == 3 and nx == sx and ny == sy:
            dfs(nx, ny, nd, cnt) # cnt + 1 안함(이미갔으니)

        if in_range(nx, ny) and not desserts[arr[nx][ny]]:
            desserts[arr[nx][ny]] = True
            dfs(nx, ny, nd, cnt + 1)
            desserts[arr[nx][ny]] = False

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    desserts = [False] * 101
    ans = -1

    for i in range(N):
        for j in range(N):
            sx, sy = i, j
            # 출발점 체크
            desserts[arr[i][j]] = True
            dfs(i, j, 0, 1) # 하나 먹으면서 시작하니 cnt = 1
            desserts[arr[i][j]] = False

    print(f'#{tc} {ans}')
