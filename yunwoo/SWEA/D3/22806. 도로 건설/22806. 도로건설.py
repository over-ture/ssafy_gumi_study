num = int(input())
for seq in range(1,num+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    row = [i for i in arr]
    col = list(map(list, zip(*arr)))
    i = 0
    j = 0
    min_val = 100
    idx = 0
    for i in range(n):
        for j in range(n):
            arr_1 = row[i]+col[j]
            arr_1.remove(arr[i][j])
            for x in range(1,6):
                result = 0
                for y in arr_1:
                    result +=abs(y-x)
                if result<=min_val:
                    min_val = result
                    idx = x
    print(f'#{seq} {min_val} {idx}')

