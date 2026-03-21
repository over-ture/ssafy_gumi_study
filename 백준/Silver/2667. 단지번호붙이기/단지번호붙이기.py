def bfs(x,y):
    global cnt
    cnt = 1
    q = [(x,y)]
    while q:
        x,y = q.pop(0)
        visited[x][y] = 1
        for ni, nj in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx = x+ni
            ny = y+nj
            if 0<=nx<n and 0<=ny<n and maze[nx][ny]==1 and visited[nx][ny]==0:
                visited[nx][ny]=1
                cnt+=1
                q.append((nx,ny))
    arr.append(cnt)
n  = int(input())
maze = [list(map(int,input().strip())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
arr = []
cnt = 0
count  = 0 
for x in range(n):
    for y in range(n):
        if maze[x][y]==1 and visited[x][y]==0:
            count+=1
            bfs(x,y)
print(count)
arr.sort()
for x in arr:
    print(x)