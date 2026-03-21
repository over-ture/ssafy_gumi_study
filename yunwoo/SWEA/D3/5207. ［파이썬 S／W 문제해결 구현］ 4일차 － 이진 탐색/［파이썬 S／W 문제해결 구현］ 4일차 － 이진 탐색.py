def bin_search(arr,low,high,key,dir):
    if low>high:
        return False
    mid = (low+high)//2
    if arr[mid]==key:
        return True
    elif arr[mid]>key:
        if dir==1:
            return False
        return bin_search(arr,low,mid-1,key,1)
    else:
        if dir==2:
            return False
        return bin_search(arr,mid+1,high,key,2)
num = int(input())
for seq in range(1,num+1):
    n,m = map(int,input().split())
    a_arr = sorted(list(map(int,input().split())))
    b_arr = list(map(int,input().split()))
    cnt = 0
    for x in b_arr:
        if bin_search(a_arr,0,n-1,x,0):
            cnt+=1
    print(f'#{seq} {cnt}')