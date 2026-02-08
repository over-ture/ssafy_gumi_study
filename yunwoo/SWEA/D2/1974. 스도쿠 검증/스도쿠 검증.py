num = int(input())
for seq in range(1, num + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    valid = True

    for i in range(9):
        row_set = set()
        col_set = set()
        for j in range(9):
            row_set.add(arr[i][j])
            col_set.add(arr[j][i])
        if len(row_set) != 9 or len(col_set) != 9:
            valid = False
            break

    if valid:
        for block_x in range(0, 9, 3):
            for block_y in range(0, 9, 3):
                block_set = set()
                for i in range(3):
                    for j in range(3):
                        num = arr[block_x + i][block_y + j]
                        block_set.add(num)
                if len(block_set) != 9:
                    valid = False
                    break
            if not valid:
                break
    if valid == True:
        print(f'#{seq} 1')
    else:
        print(f'#{seq} 0')