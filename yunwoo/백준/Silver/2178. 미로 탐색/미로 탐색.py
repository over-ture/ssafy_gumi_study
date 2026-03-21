n,m = map(int,input().split())
maze = [list(map(int,input().strip())) for _ in range(n)]
visited= [[0]*m for _ in range(n)]
visited[0][0]=1
q = []
q.append([0,0])
cnt = 0
while q:
    x,y =q.pop(0)
    if x== n-1 and y==m-1:
        print(visited[n-1][m-1])
    for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
        dx,dy = x+di,y+dj
        if 0<=dx<n and 0<=dy<m and maze[dx][dy]==1 and visited[dx][dy]==0:
            q.append([dx,dy])
            visited[dx][dy]=visited[x][y]+1
        