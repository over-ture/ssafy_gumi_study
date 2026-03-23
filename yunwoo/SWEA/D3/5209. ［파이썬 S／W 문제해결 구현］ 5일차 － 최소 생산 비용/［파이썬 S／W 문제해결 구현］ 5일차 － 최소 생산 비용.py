num = int(input())
def min_cost(lev,total):
    global min_value
    if lev ==n:
        min_value = min(min_value, total)
        return
    if total>min_value:
        return
    for i in range(n):
        if visited[i]==0:
            visited[i]=1
            min_cost(lev+1,total+maze[lev][i])
            visited[i]=0
        
for seq in range(1,num+1):
    n = int(input())
    maze = [list(map(int,input().split())) for _ in range(n)]
    min_value = 10**9
    visited= [0]*n
    min_cost(0,0)
    print(f'#{seq} {min_value}')