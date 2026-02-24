arr = [list(map(int,input().split())) for _ in range(5)]
ans = [list(map(int,input().split())) for _ in range(5)]
cnt = 0
for i in range(5):
    for j in range(5):
        for x in range(5):
            for y in range(5):
                if arr[x][y]==ans[i][j]:
                    arr[x][y]=0  
        cnt+=1
        result = 0
        for r in range(5):
            if arr[r].count(0) == 5:
                result += 1
        for c in range(5):
            cnt_1 = 0
            for j in range(5):
                if arr[j][c]==0:
                    cnt_1+=1
            if cnt_1 == 5:
                result+=1
        cnt1 = 0
        cnt2 = 0
        for k in range(5):
            if arr[k][k] == 0:
                cnt1 += 1
            if arr[k][4-k] == 0:
                cnt2 += 1
        if cnt1 == 5:
            result += 1
        if cnt2 == 5:
            result += 1
        if result >= 3:
            print(cnt)
            exit()