def check(row):
    global cnt
    
    if row == n:
        cnt += 1
        return
    
    for col in range(n):
        if not col_v[col] and not diag1[row+col] and not diag2[row-col+n]:
            col_v[col] = 1
            diag1[row+col] = 1
            diag2[row-col+n] = 1
            
            check(row+1)
            
            col_v[col] = 0
            diag1[row+col] = 0
            diag2[row-col+n] = 0

n = int(input())

col_v = [0]*n
diag1 = [0]*(2*n)
diag2 = [0]*(2*n)

cnt = 0
check(0)

print(cnt)