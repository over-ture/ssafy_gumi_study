def bfs(x,y):
    q = [(x,y)]
    visited[x][y]=1
    cnt = 1
    while q:
        x,y = q.pop(0)
        for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx = x+ni
            ny = y+nj
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and maze[nx][ny]==1:
                visited[nx][ny]=1
                q.append((nx,ny))
                cnt+=1
    return cnt
n,m,c = map(int,input().split())
maze = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]
max_val = 0
for _ in range(c):
    a,b= map(int,input().split())
    maze[a-1][b-1]=1
for i in range(n):
    for j in range(m):
        if maze[i][j]==1 and visited[i][j]==0:
            cnt = bfs(i,j)
            max_val  = max(max_val,cnt)
print(max_val)