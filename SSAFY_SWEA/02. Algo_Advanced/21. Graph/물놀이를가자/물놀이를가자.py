import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

from collections import deque
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    waters = []
    arr = []
    vis = [[float('inf')] * m for _ in range(n)]
    for i in range(n):
        temp = list(input())
        arr.append(temp)
        for j in range(m):
            if temp[j] == 'W':
                waters.append((i, j))
                vis[i][j] = 0
    q = deque(waters)
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if in_range(nx, ny) and vis[x][y] + 1 < vis[nx][ny]:
                vis[nx][ny] = vis[x][y] + 1
                q.append((nx, ny))
    tot = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W':
                continue
            else:
                tot += vis[i][j]
    print(f'#{tc} {tot}')