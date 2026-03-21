n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
arr_1 = [list(map(int,input().split())) for _ in range(n)]
for x in range(n):
    for y in range(m):
        arr[x][y]+=arr_1[x][y]
for x in range(n):
    for y in range(m):
        print(arr[x][y])
