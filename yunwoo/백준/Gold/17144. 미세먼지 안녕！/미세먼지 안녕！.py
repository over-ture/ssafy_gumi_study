import sys
input = sys.stdin.readline
def spread():
    temp = [[0]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if maze[x][y]>0:
                cnt = 0
                for ni, nj in [[0,1],[1,0],[0,-1],[-1,0]]:
                    nx = x+ni
                    ny = y+nj
                    if 0<=nx<n and 0<=ny<m and maze[nx][ny]!=-1:
                        temp[nx][ny] += maze[x][y]//5
                        cnt+=1
                temp[x][y]+=(maze[x][y]-maze[x][y]//5*cnt)
    temp[cleaner][0] = -1
    temp[cleaner+1][0] = -1
    return temp
def clean(maze,cleaner):
    top = cleaner
    bottom = cleaner + 1

    for i in range(top-1, 0, -1):
        maze[i][0] = maze[i-1][0]
    for i in range(m-1):
        maze[0][i] = maze[0][i+1]
    for i in range(top):
        maze[i][m-1] = maze[i+1][m-1]
    for i in range(m-1,1,-1):
        maze[top][i] = maze[top][i-1]
    maze[top][1] = 0

    for i in range(bottom+1, n-1):
        maze[i][0] = maze[i+1][0]
    for i in range(m-1):
        maze[n-1][i] = maze[n-1][i+1]
    for i in range(n-1, bottom, -1):
        maze[i][m-1] = maze[i-1][m-1]
    for i in range(m-1,1,-1):
        maze[bottom][i] = maze[bottom][i-1]
    maze[bottom][1] = 0

n,m,k = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(n)]
cleaner = 0
for y in range(n):
    if maze[y][0]==-1:
            cleaner = y
            break
for x in range(k):
    maze = spread()
    clean(maze,cleaner)
result = 0
for x in maze:
    result +=sum(x)
print(result+2)
    