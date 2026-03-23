from collections import deque
num = int(input())
def gravity(board):
    for j in range(w):
        idx = h-1
        for i in range(h-1,-1,-1):
            if board[i][j]:
                board[i][j],board[idx][j] = board[idx][j],board[i][j]
                idx-=1
def count_brick(board):
    cnt = 0
    for i in range(h):
        for j in range(w):
            if board[i][j]>0:
                cnt+=1
    return cnt
def bomb(x,y,board):
    q = deque()
    val = board[x][y]
    board[x][y] = 0
    q.append((x, y, val))
    while q:
        x,y,pow = q.popleft()
        for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]]:
            for p in range(1, pow):
                nx = x + ni*p
                ny = y + nj*p
                if 0<=nx<h and 0<=ny<w:
                    if board[nx][ny]>0:
                        if board[nx][ny]>1:
                            q.append((nx,ny,board[nx][ny]))
                        board[nx][ny]=0
def search(n,maze):
    for i in range(h):
        if maze[i][n]>0:
            return i
    return -1
def dfs(cnt,maze):
    global min_val
    if min_val == 0:
        return 
    if cnt == n:
        total_brick = count_brick(maze)
        min_val = min(min_val,total_brick)
        return
    for y in range(w):
        dest = [row[:] for row in maze]
        r = search(y, dest)
        if r!=-1:
            bomb(r,y,dest)
            gravity(dest)
            dfs(cnt + 1, dest)
        else:
            dfs(cnt+1,dest)
for seq in range(1,num+1):
    n,w,h = map(int,input().split())
    maze = [list(map(int,input().split())) for _ in range(h)]
    min_val = 10**9
    dfs(0,maze)
    print(f'#{seq} {min_val}')