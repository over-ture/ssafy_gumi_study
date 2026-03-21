def dfs(i,j):
    visited = [[0]*m for _ in range(n)]
    stack = []
    stack.append((i,j))
    visited[i][j]=1
    while stack:
        x,y = stack.pop()
        if x == n-1:
            return 1
        for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx = x+ni
            ny = y+nj
            if 0<=nx<n and 0<=ny<m and maze[nx][ny]==0 and visited[nx][ny]==0:
                stack.append((nx,ny))
                visited[nx][ny]=1
    return 0                 
n, m =map(int,input().split())
maze = [list(map(int,input().strip())) for _ in range(n)]
start = []
cnt = 0
for x in maze[0]:
    if x==0:
        start.append((0,cnt))
    cnt+=1
result = 0
for x,y in start:
    result = dfs(x,y)
    if result ==1:
        break
if result==1:
    print("YES")
else:
    print("NO")