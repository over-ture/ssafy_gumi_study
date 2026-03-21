from collections import deque
 
def bfs(sx, sy, n, maze):
    q = deque([(sx, sy)])
    v = [[0] * n for _ in range(n)] 
    v[sx][sy] = 1
    cnt = 0 
     
    while q:
        x, y = q.popleft()
        cnt += 1
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = x + dx, y + dy
            if 0 <= ni < n and 0 <= nj < n and not v[ni][nj]:
                if maze[ni][nj] == maze[x][y] + 1:
                    v[ni][nj] = 1
                    q.append((ni, nj))
    return cnt
 
num = int(input())
for seq in range(1, num + 1):
    n = int(input())
    maze = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = 0
    start_room = float('inf')
    for x in range(n):
        for y in range(n):
            current_cnt = bfs(x, y, n, maze)
 
            if current_cnt > max_cnt:
                max_cnt = current_cnt
                start_room = maze[x][y]
            elif current_cnt == max_cnt:
                if maze[x][y] < start_room:
                    start_room = maze[x][y]             
    print(f'#{seq} {start_room} {max_cnt}')
