num = int(input())
for seq in range(1,num+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(m):
        i, j = map(int, input().split())
        i-=1
        for x in range(j,0,-1):
            if i-x<0:
                continue
            elif i+x>len(arr)-1:
                continue
            else:

                if arr[i-x] == arr[i+x] and arr[i-x] == 1:
                    arr[i-x] = 0
                    arr[i+x] = 0
                elif arr[i-x] == arr[i+x] and arr[i-x]==0:
                    arr[i-x] = 1
                    arr[i+x] = 1
                else :
                    continue
    print(f'#{seq} ', end ="")
    print(*arr)
