def check(cnt):
    if cnt == result:
        for x in maze:
            print(*x)
        exit()
    x,y = zero[cnt]
    for i in range(1,10):
        if used[x][i]==0 and used_1[y][i]==0 and used_2[(x//3)*3+(y//3)][i]==0: 
            maze[x][y]=i
            used[x][i]=1
            used_1[y][i]=1
            used_2[(x//3)*3+(y//3)][i]=1
            check(cnt+1)
            maze[x][y]=0
            used[x][i]=0
            used_1[y][i]=0
            used_2[(x//3)*3+(y//3)][i]=0


maze = [list(map(int,input().split())) for _ in range(9)]
zero = []
result = 0
used =[[0]*10 for _ in range(9)]
used_1 =[[0]*10 for _ in range(9)]
used_2 =[[0]*10 for _ in range(9)]
cnt = 0
for x in range(9):
    for y in range(9):
        if maze[x][y]==0:
            zero.append((x,y))
            result+=1
        else:
            used[x][maze[x][y]]=1
            used_1[y][maze[x][y]]=1
            used_2[(x//3)*3+(y//3)][maze[x][y]]=1      
check(cnt)

