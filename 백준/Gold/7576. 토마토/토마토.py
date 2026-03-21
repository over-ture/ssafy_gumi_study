import sys
from collections import deque

def bfs():
    while q:
        x,y = q.popleft()
        for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx = x+ni
            ny = y+nj
            if 0<=nx<n and 0<=ny<m and maze[nx][ny]==0:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx,ny))

m,n = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(n)]
q = deque()

for x in range(n):
    for y in range(m):
        if maze[x][y] == 1:
            q.append((x,y))

bfs()

result = 0
for x in range(n):
    for y in range(m):
        if maze[x][y] == 0:
            print(-1)
            exit()
        result = max(result, maze[x][y])

print(result-1)