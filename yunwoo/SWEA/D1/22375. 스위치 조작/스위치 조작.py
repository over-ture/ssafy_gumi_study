num = int(input())
for seq in range(1, num+1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr_1 = list(map(int, input().split()))
    i = 0
    cnt = 0
    while i < n:
        if arr[i]==arr_1[i]:
            i += 1
        else:
            for x in range(i,n):
                if arr[x] == 0:
                    arr[x]=1
                else:
                    arr[x] = 0
            i+=1
            cnt +=1
    print(f'#{seq} {cnt}')
        
    