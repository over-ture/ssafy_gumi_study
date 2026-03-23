dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1] # 상 우 하 좌 (시계)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

mapping = {
    1 : [0,1,2,3], # 상하좌우
    2 : [0,2], # 상하
    3 : [1,3], # 좌우
    4 : [0,1], # 우상
    5 : [1,2], # 우하
    6 : [2,3], # 좌하
    7 : [0,3], # 좌상
}

connected = [ # 상 우 하 좌
    [1,2,5,6], # 윗쪽으로 갈 때 : 아래가 뚫린 블럭들
    [1,3,6,7],
    [1,2,4,7],
    [1,3,4,5],
]

def bfs(r, c, l):
    q = [(r, c, 1)]
    vis[r][c] = True

    while q:
        r, c, t = q.pop(0)

        if t == l:
            break

        for d in mapping[arr[r][c]]:
            nr, nc = r + dr[d], c + dc[d]
            if in_range(nr, nc) and not vis[nr][nc] and arr[nr][nc] in connected[d]:
                vis[nr][nc] = True
                q.append((nr,nc,t+1))


T = int(input())
for tc in range(1,T+1):
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    vis = [[False] * m for _ in range(n)]
    cnt = 0
    bfs(r,c,l)
    for i in range(n):
        for j in range(m):
            if vis[i][j]:
                cnt += 1
    print(f'#{tc} {cnt}')