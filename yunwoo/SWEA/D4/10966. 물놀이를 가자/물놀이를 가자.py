from collections import deque
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(input().strip()) for _ in range(n)]
    visited = [[-1]*m for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W':
                visited[i][j] = 0
                q.append((i, j))
    
    while q:
        x, y = q.popleft()
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    
    result = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'L':
                result += visited[i][j]
    
    print(f'#{tc} {result}')