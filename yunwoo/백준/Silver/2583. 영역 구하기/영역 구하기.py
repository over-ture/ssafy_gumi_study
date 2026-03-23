def bfs(x,y):
    cnt = 1
    q = [(x,y)]
    visited[x][y]=1
    while q:
        x,y=q.pop(0)
        visited[x][y]=1
        for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx = x + ni
            ny = y + nj
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and maze[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y]+1
                cnt+=1
    return cnt

m,n,k = map(int,input().split())
maze = [[0]*m for _ in range(n)]
for _ in range(k):
    a,b,c,d = map(int,input().split())
    for x in range(a,c):
        for y in range(b,d):
            maze[x][y]=1
visited = [[0]*m for _ in range(n)]
arr = []
for x in range(n):
    for y in range(m):
        if maze[x][y]==0 and visited[x][y]==0:
            cnt = bfs(x,y)
            arr.append(cnt)
print(len(arr))
print(*sorted(arr))
  
