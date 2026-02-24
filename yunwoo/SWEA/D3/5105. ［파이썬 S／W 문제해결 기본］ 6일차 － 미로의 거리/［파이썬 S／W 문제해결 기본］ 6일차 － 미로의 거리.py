num = int(input())
def bfs(x,y,n):
    visited =[[0]*n for _ in range(n)]
    q = []
    q.append([x,y])
    visited[x][y] = 1
    while q:
        ti, tj = q.pop(0)
        if maze [ti][tj] == 2:
            return visited[ti][tj]-2
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            wi, wj = ti+di, tj+dj
            if 0<=wi<n and 0<=wj<n and maze[wi][wj]!= 1 and visited[wi][wj] == 0 :
                q.append([wi,wj])
                visited[wi][wj]= visited[ti][tj]+1
    return 0 
        
for seq in range(1,num+1):
    n = int(input())
    maze = [list(map(int,input())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maze[i][j]==3:
                x = i
                y = j
    result = bfs(x,y,n)
    print(f'#{seq} {result}')