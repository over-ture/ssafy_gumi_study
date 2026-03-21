def bfs(x,y):
    q = [(x,y)]
    visited[x][y]=1
    while q:
        x,y=q.pop(0)
        visited[x][y]=1
        for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx = x+ni
            ny = y+nj
            if 0<=nx<n and 0<=ny<m and maze[nx][ny]==1 and visited[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny]=1
n = int(input())
for _ in range(n):
    n,m,a = map(int,input().split())
    maze = [[0]*m for _ in range(n)]
    for _ in range(a):
        c,d = map(int,input().split())
        maze[c][d]=1
    visited=[[0]*m for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(m):
            if visited[x][y]==0 and maze[x][y]==1:
                cnt+=1
                bfs(x,y)
    print(cnt)