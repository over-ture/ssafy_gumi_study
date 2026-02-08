T= int(input())
for i in range(1,T+1):
    N,M = map(int, input().split())
    arr = list(map(int,input().split()))
    max_v = 0
    min_v = 0
    for a in range(M):
        max_v += arr[a]
        min_v += arr[a]
    for j in range(1,N-M+1):
        b = 0
        for c in range(j,j+M):
            b+=arr[c]
        if max_v<b:
            max_v = b
        if min_v>b:
             min_v = b
    print(f'#{i} {max_v-min_v}')