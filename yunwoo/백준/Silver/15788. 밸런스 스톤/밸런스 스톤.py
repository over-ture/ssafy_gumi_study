n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
col_sum = [0]*n  
for i in range(n):
    for j in range(n):
        col_sum[j] += arr[i][j]
        if arr[i][j]== 0:
            x,y = i,j 
            target = sum(arr[i])
max_val = max(col_sum)
arr[x][y]= max_val  - target
flag = True
col_sums = [0]*n
for i in range(n):
    if sum(arr[i]) != max_val:
        flag = False
        break
    for j in range(n):
        col_sums[j] += arr[i][j]

if flag:
    for j in range(n):
        if col_sums[j] != max_val:
            flag = False
            break

if flag:
    cnt = sum(arr[i][i] for i in range(n))
    cnt_1 = sum(arr[i][n-1-i] for i in range(n))
    if cnt != max_val or cnt_1 != max_val:
        flag = False

if flag:
    print(arr[x][y])
else:
    print(-1)

            



            

