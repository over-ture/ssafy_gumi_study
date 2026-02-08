number = int(input())
for seq in range(1, number + 1):
    num, count = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(num)]
    result = 0
    row = []
    col = []
    for i in range(num):
        row_count = 0
        col_count = 0
        for j in range(num):
            if arr[i][j] == 1:
                row_count += 1
                if j == num-1:
                    row.append(row_count)
                    row_count = 0
            else:
                if row_count>=1:
                    row.append(row_count)
                row_count = 0
            if arr[j][i] == 1:
                col_count += 1
                if j==num-1:
                    col.append(col_count)
                    col_count = 0
            else:
                if col_count >= 1:
                    col.append(col_count)
                col_count = 0
    for i in row:
        if i ==count :
            result+=1
    for i in col:
        if i ==count:
            result+=1

    print(f'#{seq} {result}')
