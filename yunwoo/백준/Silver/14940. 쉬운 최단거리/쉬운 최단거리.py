def bfs(x,y):
    q = [(x,y)]
    visited[x][y]=0
    while q:
        x,y=q.pop(0)
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx = x+di
            ny = y+dj
            if 0<=nx<n and 0<=ny<m and maze[nx][ny]==1 and visited[nx][ny]==-1:
                q.append((nx,ny))
                visited[nx][ny]= visited[x][y]+1
        
n,m = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
a,b=0,0
for x in range(n):
    for y in range(m):
        if maze[x][y]==0:
            visited[x][y]=0
        if maze[x][y]==2:
            a,b=x,y
bfs(a,b)
for x in range(n):
    for y in range(m):
        print(visited[x][y], end=" ")
    print()