import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

length = 0

def bfs(r,c):
    dist = 0
    visited = [[-1]*C for _ in range(R)]
    q = deque()
    q.append([r,c])
    visited[r][c] = 0

    while q:
        tr, tc = q.popleft()

        for dr, dc in [[0,1],[1,0],[0,-1],[-1,0]]:
            nr = tr + dr
            nc = tc + dc
            if 0<=nr<R and 0<=nc<C and visited[nr][nc]==-1 and arr[nr][nc]=='L':
                q.append([nr,nc])
                visited[nr][nc] = visited[tr][tc] + 1
                dist = max(dist, visited[nr][nc])

    return dist


for r in range(R):
    for c in range(C):
        if arr[r][c]=='L':
            length = max(length, bfs(r,c))
print(length)