import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
flag = False

def dfs(y, x):
    global flag

    if y == M - 1:
        flag = True
        return True
    
    grid[y][x] = 9
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < M and 0 <= nx < N and grid[ny][nx] == 0:
            dfs(ny, nx)

M, N = map(int, input().split())
grid = []

for _ in range(M):
    grid.append(list(map(int, input().rstrip())))

for x in range(N):
    if grid[0][x] == 0:
        dfs(0, x)
        if flag:
            print('YES')
            break
if not flag:
    print('NO')
