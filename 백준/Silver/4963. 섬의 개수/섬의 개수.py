def dfs(x,y):
    global cnt
    stack = []
    visited[x][y]=cnt
    stack.append((x,y))
    while stack:
        x,y = stack.pop()
        for ni,nj in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]:
            nx = x+ni
            ny = y+nj
            if 0<=nx<h and 0<=ny<w and visited[nx][ny]==0 and arr[nx][ny]==1:
                stack.append((nx,ny))
                visited[nx][ny]=1
while True:
    w,h = map(int,input().split())
    if w==0 and h==0:
        break
    arr = [list(map(int,input().split())) for _ in range(h)]
    visited=[[0]*w for _ in range(h)]
    cnt = 0
    for x in range(h):
        for y in range(w):
            if arr[x][y] == 1 and visited[x][y] == 0:
                cnt += 1
                dfs(x,y)
    print(cnt)