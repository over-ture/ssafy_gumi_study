num = int(input())

def bfs(x, y):
    global cnt
    q = [(x, y, 1)]
    visited[x][y] = 1
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    pipe = {
        1: [0, 1, 2, 3], 2: [1, 3], 3: [0, 2], 4: [0, 3],
        5: [0, 1], 6: [1, 2], 7: [2, 3]
    }

    while q:
        x, y, time = q.pop(0)
        
        if time == l:
            continue
        curr_p = maze[x][y]
        for i in pipe[curr_p]:
            ni = x + dx[i]
            nj = y + dy[i]
            if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] != 0 and visited[ni][nj] == 0:
                next_p = maze[ni][nj]
                if (i + 2) % 4 in pipe[next_p]:
                    visited[ni][nj] = 1
                    q.append((ni, nj, time + 1))

for seq in range(1, num + 1):
    n, m, r, c, l = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    bfs(r, c)
    result = 0
    for row in visited:
        result += sum(row)
    print(f'#{seq} {result}')