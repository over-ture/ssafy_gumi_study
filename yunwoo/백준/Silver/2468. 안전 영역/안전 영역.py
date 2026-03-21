
def dfs(x, y, h):
    stack = [(x, y)]
    visited[x][y] = 1
    while stack:
        x, y = stack.pop()
        for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx = x + dx
            ny = y + dy       
            if 0 <= nx < n and 0 <= ny < n:
                if maze[nx][ny] > h and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    stack.append((nx, ny))

n = int(input())
maze = [list(map(int,input().split())) for _ in range(n)]
max_height = max(max(row) for row in maze)
result = 0
for h in range(max_height + 1):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if maze[i][j] > h and visited[i][j] == 0:
                dfs(i, j, h)
                cnt += 1
    result = max(result, cnt)
print(result)