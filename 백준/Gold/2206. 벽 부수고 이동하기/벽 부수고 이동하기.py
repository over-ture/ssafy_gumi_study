from collections import deque

dr, dc = [-1,0,1,0], [0,1,0,-1]

def bfs():
    vis = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
    vis[0][0][0] = 0
    q = deque([(0,0,0)])

    while q:
        r, c, w = q.popleft()

        if r == n-1 and c == m-1:
            return vis[r][c][w] + 1
        
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0<=nr<n and 0<=nc<m:
                if arr[nr][nc] == 0 and vis[nr][nc][w] == -1:
                    vis[nr][nc][w] = vis[r][c][w] + 1
                    q.append((nr,nc,w))

                elif arr[nr][nc] == 1 and w == 0 and vis[nr][nc][1] == -1: # 벽 안 부쉈는데 벽 만났으면
                    vis[nr][nc][1] = vis[r][c][0] + 1
                    q.append((nr,nc,1))
            
    return -1

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
print(bfs())
