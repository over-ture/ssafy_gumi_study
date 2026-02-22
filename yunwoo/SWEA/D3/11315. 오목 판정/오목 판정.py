num = int(input())
for seq in range(1,num+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    row = [i for i in arr]
    col = [[arr[i][j] for i in range(n)] for j in range(n)]
    result = "NO"

    for i in row:
        cnt = 0
        for j in i:
            if j!="o":
                cnt = 0
            else:
                cnt+=1
            if cnt==5:
                result = "YES"
                break

    for j in col:
        cnt_1 = 0
        for i in j:
            if i != "o":
                cnt_1 = 0
            else:
                cnt_1 += 1
            if cnt_1 == 5:
                result = "YES"
                break
    for i in range(n):
        for j in range(n):
            if arr[i][j] == "o":
                cnt = 1
                ni, nj = i, j
                while 0 <= ni + 1 < n and 0 <= nj + 1 < n and arr[ni + 1][nj + 1] == "o":
                    cnt += 1
                    ni += 1
                    nj += 1
                if cnt >= 5:
                    result = "YES"
                cnt = 1
                ni, nj = i, j
                while 0 <= ni + 1 < n and 0 <= nj - 1 < n and arr[ni + 1][nj - 1] == "o":
                    cnt += 1
                    ni += 1
                    nj -= 1
                if cnt >= 5:
                    result = "YES"
    print(f'#{seq} {result}')

