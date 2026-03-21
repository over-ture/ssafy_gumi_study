D = [[0,1],[1,0],[0,-1],[-1,0]]
def dfs(x, y, number,depth):
    if depth == 7:
        result.add(number)
        return
    for dx,dy in D:
        ni, nj = x + dx, y + dy
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(ni, nj, number*10+maze[ni][nj],depth+1)

num = int(input())
for seq in range(1,num+1):
    maze = [list(map(int,input().split())) for _ in range(4)]
    result = set()
    for x in range(4):
        for y in range(4):
            dfs(x,y,maze[x][y],1)


    print(f'#{seq} {len(result)}')