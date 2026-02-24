num = int(input())
for seq in range(1,num+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                s= arr[i][j]
                for di,dj in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]] :
                    for c in range(1,50):
                        ni = i +di*c
                        nj = j +dj*c
 
                        if 0 <= ni< n and 0 <= nj <n:
                            if arr[ni][nj] == 1 or arr[ni][nj] == 3:
                                break
                            elif arr[ni][nj] == 2:
                                cnt += 1
    print(f'#{seq} {cnt}')