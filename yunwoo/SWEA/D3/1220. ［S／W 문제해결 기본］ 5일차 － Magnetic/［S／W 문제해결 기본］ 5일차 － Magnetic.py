for seq in range(1,11):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = 0
    for j in range(n):
        for i in range(n):
            if arr[i][j] ==1:
                x = i+1
                cnt = 0
                while x<n:
                    if arr[x][j]==2:
                        result+=1
                        break
                    elif arr[x][j]==1:
                        arr[x][j]=0
                    x+=1
    print(f'#{seq} {result}')


