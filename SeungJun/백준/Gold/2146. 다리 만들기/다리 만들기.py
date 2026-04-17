from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [-1, 0, 1, 0], [0, 1 ,0, -1]
def in_range(x,y):
    return 0<=x<n and 0<=y<n

def island_indexing(r,c, idx): # 섬 인덱싱
    q = deque([(r,c)])
    vis[r][c] = True
    arr[r][c] = idx
    island_pos.append((r, c)) # 섬의 좌표를 저장

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if in_range(nx, ny) and not vis[nx][ny] and arr[nx][ny] == 1:
                vis[nx][ny] = True
                arr[nx][ny] = idx
                q.append((nx, ny))
                island_pos.append((nx, ny))  

def bridge(idx, pos): # 각 섬 별 다리 건설
    q = deque([])
    dist = [[-1] * n for _ in range(n)]

    for r, c in pos:
        dist[r][c] = 0
        q.append((r, c))

    for i in range(n):
        for j in range(n):
            if arr[i][j] == idx:
                q.append((i,j))
                dist[i][j] = 0

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if in_range(nx, ny):
                if arr[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                # 다른 섬을 만난 경우
                elif arr[nx][ny] != 0 and arr[nx][ny] != idx:
                    return dist[x][y]
    
    return 10**4

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 10**4
vis = [[False] * n for _ in range(n)]
islands = []
idx = 2
for i in range(n):
    for j in range(n):
        if not vis[i][j] and arr[i][j] == 1:
            island_pos = []
            island_indexing(i, j, idx)
            islands.append((idx, island_pos))
            idx += 1

for idx, pos in islands:
    ans = min(ans, bridge(idx, pos))

print(ans)