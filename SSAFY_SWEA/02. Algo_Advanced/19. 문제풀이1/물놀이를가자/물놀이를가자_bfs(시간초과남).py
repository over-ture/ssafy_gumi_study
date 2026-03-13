import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

from collections import deque

# 코드
drs, dcs = [-1, 0, 1, 0], [0, 1, 0, -1]
def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

def bfs(R,C,Dist):
    vis[R][C] = Dist
    q = deque([(R, C, Dist)])
    while q:
        r, c, dist = q.popleft()
        for d in range(4):
            nr, nc = r + drs[d], c + dcs[d]
            if in_range(nr, nc) and dist + 1 < vis[nr][nc]:
                vis[nr][nc] = dist + 1
                q.append((nr, nc, dist+1))

T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())
    water = []
    land = []
    for i in range(n):
        temp = input()
        for j in range(m):
            if temp[j] == 'W':
                water.append((i, j)) # 물 위치 찾기
            elif temp[j] == 'L':
                land.append((i,j))
    vis = [[float('inf')] * m for _ in range(n)]
    for r, c in water:
        bfs(r, c, 0)
    ans = 0
    for r, c in land:
        ans += vis[r][c]
    print(f'#{tc} {ans}')