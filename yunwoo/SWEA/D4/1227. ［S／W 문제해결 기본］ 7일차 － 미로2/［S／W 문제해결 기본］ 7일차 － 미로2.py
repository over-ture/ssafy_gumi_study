def bfs(x,y):
    visited =[[0]*100 for _ in range(100)]
    q = []
    q.append([x,y])
    visited[x][y]= 1
    while q:
        ti, tj = q.pop(0)
        if arr[ti][tj]==3:
            return 1
        for di ,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            wi, wj = ti+di, tj+dj
            if 0<=wi<100 and 0<=wj<100 and arr[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])  
                visited[wi][wj]=1
    return 0     
for _ in range(10):
    seq = int(input())
    arr = [list(map(int,input())) for _ in range(100)]
    for i in range(100):
        if 2 in arr[i]:
            x = i
            y = arr[i].index(2)
            break
    result = bfs(x,y)
    print(f'#{seq} {result}')