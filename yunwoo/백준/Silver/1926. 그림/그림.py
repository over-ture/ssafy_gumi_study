def bfs(x,y):
    cnt=1
    q = [(x,y)]
    while q:
        x,y = q.pop(0)
        visited[x][y]=1
        for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx = x+ni
            ny = y+nj
            if 0<=nx<n and 0<=ny<m and maze[nx][ny]==1 and visited[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny]=1
                cnt+=1
    return cnt
n,m = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
result = 0
cont=0
for x in range(n):
    for y in range(m):
        if maze[x][y]==1 and visited[x][y]==0:
            cnt = bfs(x,y)
            result = max(result, cnt)
            cont+=1
print(cont)
print(result)