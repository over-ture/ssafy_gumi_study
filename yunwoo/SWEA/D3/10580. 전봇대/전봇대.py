num = int(input())
for seq in range(1,num+1):
    n = int(input())
    pool = []
    for _ in range(n):
        a,b = map(int,input().split())
        pool.append([a,b])
    cnt = 0
    pool.sort()
    for i in range(n):
        for j in range(i,n):
            if pool[i][1] >pool[j][1]:
                cnt+=1
    print(f'#{seq} {cnt}')
    