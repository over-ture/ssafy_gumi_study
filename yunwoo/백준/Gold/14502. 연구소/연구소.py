import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque
from itertools import combinations
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs():
    global max_val
    q = deque(virus)
    visited = [[0]*m for _ in range(n)]
    cnt = 0
    while q:
        x,y = q.popleft()
        visited[x][y]=1
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]==0 and visited[nx][ny]==0:
                visited[nx][ny]=1
                q.append((nx,ny))
    for x in range(n):
        for y in range(m):
            if arr[x][y] == 0 and visited[x][y] == 0:
                cnt+=1
    max_val = max(max_val,cnt)
    
def build(cnt,start):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                build(cnt+1)
                arr[i][j] = 0

n,m = map(int,input().split())
arr= [list(map(int,input().split())) for _ in range(n)]
virus = []
empty = []
max_val = 0
for x in range(n):
    for y in range(m):
        if arr[x][y]==2:
            virus.append((x,y))
        if arr[x][y]==0:
            empty.append((x,y))
for walls in combinations(empty, 3):
    for wx, wy in walls:
        arr[wx][wy] = 1
    bfs()
    for wx, wy in walls:
        arr[wx][wy] = 0
print(max_val)
