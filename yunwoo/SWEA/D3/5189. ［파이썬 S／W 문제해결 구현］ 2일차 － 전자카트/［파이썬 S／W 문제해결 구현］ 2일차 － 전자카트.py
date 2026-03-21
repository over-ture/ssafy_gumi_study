num = int(input())
def kfc(x,cnt,sum_result):
    global min_val
    if cnt == n:
        sum_result+=maze[x][0]
        min_val = min(min_val,sum_result)
    if sum_result>=min_val:
        return
    for i in range(1,n):
        if not visited[i]:
            visited[i]=1
            kfc(i,cnt+1,sum_result+maze[x][i])
            visited[i]=0
        
for seq in range(1,num+1):
    n = int(input())
    maze = [list(map(int,input().split())) for _ in range(n)]
    visited = [0]*n
    visited[0]=1
    min_val = 100000000
    kfc(0,1,0)
    print(f'#{seq} {min_val}')