n,m = map(int,input().split())
arr = [[0]*m for _ in range(n)]
x = 0
y=0 
idx = 0
arr[0][0]=1
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for cnt in range(2, n*m+1):
    nx = x + dx[idx]
    ny = y + dy[idx]
    if not (0<=nx<n and 0<=ny<m and arr[nx][ny]==0):
        idx = (idx+1)%4
        nx = x + dx[idx]
        ny = y + dy[idx]
    arr[nx][ny] = cnt
    x,y = nx,ny
ans = int(input())
if ans > n*m+1:
    print(0)
else:
    for i in range(n):
        for j in range(m):
            if arr[i][j]==ans:
                print(i+1, j+1)