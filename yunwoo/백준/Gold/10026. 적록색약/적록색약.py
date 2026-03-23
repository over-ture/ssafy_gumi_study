import copy
def bfs(x,y,color):
    q = [(x,y)]
    visited[x][y]=1
    while q:
        x,y = q.pop(0)
        for ni, nj in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx = x+ni
            ny = y+nj
            if 0<=nx<n and 0<=ny<n and maze[nx][ny]==color and visited[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny]=1
                
def bfs_1(x,y,color):
    q_1 = [(x,y)]
    visited_1[x][y]=1
    while q_1:
        x,y = q_1.pop(0)
        for ni, nj in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx = x+ni
            ny = y+nj
            if 0<=nx<n and 0<=ny<n and maze_1[nx][ny]==color and visited_1[nx][ny]==0:
                q_1.append((nx,ny))
                visited_1[nx][ny]=1            
        
n = int(input())
maze = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
maze_1 = copy.deepcopy(maze)
visited_1 = [[0]*n for _ in range(n)]
cnt = 0
cnt_1 = 0
for x in range(n):
    for y in range(n):
        if maze_1[x][y]=="R":
            maze_1[x][y]="G"
        if visited[x][y]==0:
            bfs(x,y,maze[x][y])
            cnt +=1
for x in range(n):
    for y in range(n):
        if visited_1[x][y]==0:
            bfs_1(x,y,maze_1[x][y])
            cnt_1+=1      

print(cnt,cnt_1)