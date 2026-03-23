def queen(row):
    global cnt
    if row ==n:
        cnt+=1
        return
    for col in range(n):
        if used_1[col]==0 and used_2[row+col]==0 and used_3[row-col+n]==0:
            used_1[col]=1
            used_2[row+col]=1
            used_3[row-col+n]=1
            queen(row+1)
            used_1[col]=0
            used_2[row+col]=0
            used_3[row-col+n]=0
num = int(input())
for seq in range(1,num+1):
    cnt = 0
    n = int(input())
    used_1 = [0]*(n)
    used_2 = [0]*(2*n)
    used_3 = [0]*(2*n)
    queen(0)
    print(f'#{seq} {cnt}')