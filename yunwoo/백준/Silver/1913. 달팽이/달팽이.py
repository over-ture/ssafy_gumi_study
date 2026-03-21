import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
visited = [[0]*n for _ in range(n)]
maze = [[0]*n for _ in range(n)]
x,y=0,0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
maze[x][y]=n*n
visited[x][y]=1
cnt=1
while cnt<n*n:
        for num in range(4):
            nx = dx[num]+x
            ny = dy[num]+y
            while 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                x = nx
                y = ny
                maze[nx][ny]= n*n-cnt
                visited[nx][ny]=1
                nx+=dx[num]
                ny+=dy[num]
                cnt+=1
px,py=0,0
for x in range(n):
    for y in range(n):
        print(maze[x][y],end=" ")
        if maze[x][y]==m:
             px = x
             py = y
    print()
print(px+1,py+1)