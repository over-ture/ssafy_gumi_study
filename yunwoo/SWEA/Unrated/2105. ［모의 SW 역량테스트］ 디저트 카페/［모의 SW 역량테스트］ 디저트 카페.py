dx = [1,1,-1,-1]
dy = [1,-1,-1,1]
num  = int(input())
def kfc(x,y,cnt,dir):
    global max_val, start_x,start_y
    ni = x+dx[dir]
    nj = y+dy[dir]
    if dir == 3 and ni==start_x and nj == start_y:
        max_val = max(max_val,cnt)
        return
    if 0<=ni<n and 0<=nj<n and visited[maze[ni][nj]]==0:
        visited[maze[ni][nj]]=1
        kfc(ni,nj,cnt+1,dir)
        if dir<3:
            kfc(ni,nj,cnt+1,dir+1)
        visited[maze[ni][nj]]=0

for seq in range(1,num+1):
    n = int(input())
    maze = [list(map(int,input().split())) for _ in range(n)]
    max_val = -1
    for x in range(n-2):
        for y in range(1,n-1):
            start_x, start_y = x, y
            visited= [0]*101
            visited[maze[x][y]]=1
            kfc(x,y,1,0)
    print(f'#{seq} {max_val}')