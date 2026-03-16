import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)


dx, dy = [-1,0,1,0],[0,1,0,-1]

def dfs(r,c,num):
    if len(num) == 7:
        result.add(num)
        return
    for d in range(4):
        nr, nc = r + dx[d], c + dy[d]
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr,nc,num+arr[nr][nc])

T = int(input())
for tc in range(1,T+1):
    result = set()
    arr = [list(input().split()) for _ in range(4)]
    for i in range(4):
        for j in range(4):
            dfs(i,j,'')
    print(f'#{tc} {len(result)}')