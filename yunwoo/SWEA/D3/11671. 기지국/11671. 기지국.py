num = int(input())
for seq in range(1,num+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    cnt = set()
    count = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j]=="H":
                count+=1
            if arr[i][j] in "ABC":
                for di, dj in [[0, 1],[1, 0],[0, -1],[-1, 0]]:
                    for c in range(1,ord(arr[i][j])-63):
                        ni = i + di * c
                        nj = j + dj * c

                        if 0 <= ni < n and 0 <= nj < n:
                            if arr[ni][nj] == "H":
                                cnt.add((ni,nj))

    print(f'#{seq} {count-len(cnt)}')

