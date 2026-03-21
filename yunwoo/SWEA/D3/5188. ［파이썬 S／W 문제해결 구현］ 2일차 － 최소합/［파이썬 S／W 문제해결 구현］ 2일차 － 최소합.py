num = int(input())
def KFC(x,y,sum_result):
    global min_val
    if sum_result>=min_val:
        return
    if x==n-1 and y==n-1:
        min_val = min(min_val, sum_result)
        return
    for dx, dy in [[0, 1], [1, 0]]:
        ni, nj = x + dx, y + dy
        if 0 <= ni < n and 0 <= nj < n:
            if not visited[ni][nj]:
                visited[ni][nj] = 1
                KFC(ni, nj, sum_result + maze[ni][nj])
                visited[ni][nj] = 0         

        
for seq in range(1,num+1):
    min_val = 10000
    n  = int(input())
    maze = [list(map(int,input().split())) for _ in range(n)]
    visited = [[0]* n for _ in range(n)]
    visited[0][0]=1
    KFC(0,0,maze[0][0])
    print(f"#{seq} {min_val}")