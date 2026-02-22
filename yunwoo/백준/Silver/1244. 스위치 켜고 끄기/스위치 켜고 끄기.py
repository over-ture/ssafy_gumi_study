n = int(input())
arr = list(map(int, input().split()))
num = int(input())
for _ in range(num):
    a,b = map(int,input().split())
    if a==1:
        for idx in range(n):
            if (idx+1)%b==0 and arr[idx]==1:
                arr[idx] = 0
            elif (idx+1)%b==0 and arr[idx]==0:
                arr[idx] =1
    elif a==2:
        if arr[b-1]==0:
            arr[b-1] = 1
        elif arr[b-1]==1:
            arr[b-1] = 0
        cnt = 1
        while 0<=b-1-cnt and b-1+cnt<n:
            if arr[b-1-cnt]== arr[b-1+cnt] and arr[b-1-cnt]==0:
                arr[b-1-cnt],arr[b-1+cnt]=1,1
            elif arr[b-1-cnt]== arr[b-1+cnt] and arr[b-1-cnt]==1:
                arr[b-1-cnt],arr[b-1+cnt]=0,0
            elif arr[b-1-cnt]!= arr[b-1+cnt]:
                break
            cnt+=1
for i in range(0, n, 20):
    print(*arr[i:i+20])
