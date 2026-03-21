num = int(input())
def bfs(a,b,x1,y1):
    q = [(a,b)] 
    visited[a][b]=1
    cnt = 0
    while q:
        x,y = q.pop(0)
        if x == x1 and y==y1:
            return visited[x1][y1]-1
        for ni,nj in [[2,1],[1,2],[-1,2],[-2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]:
            nx = x+ni
            ny = y+nj
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1
for _ in range(num):
    n = int(input())
    visited = [[0]*n for _ in range(n)]
    s_x, s_y = map(int,input().split())
    e_x, e_y = map(int,input().split())
    result = bfs(s_x,s_y,e_x,e_y)
    print(result)    
