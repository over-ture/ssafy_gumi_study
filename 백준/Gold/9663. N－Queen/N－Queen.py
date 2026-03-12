def set_queen(row, col):
    # vis_row[row] = 1
    vis_col[col] = 1
    vis_x[row+col] = 1
    vis_negx[row-col + n-1] = 1
    
def nqueen(row):
    global cnt
    if row == n:
        cnt += 1
        return
    for c in range(n):
        if not vis_col[c] and not vis_x[row+c] and not vis_negx[row-c+n-1]:
            set_queen(row,c)
            nqueen(row+1)
            vis_col[c] = vis_x[row+c] = vis_negx[row-c+n-1] = 0


n = int(input())
vis_row = [0] * n
vis_col = [0] * n
vis_x = [0] * (2*(n-1) + 1)
vis_negx = [0] * (2*(n-1) + 1)
cnt = 0
nqueen(0)
print(cnt)