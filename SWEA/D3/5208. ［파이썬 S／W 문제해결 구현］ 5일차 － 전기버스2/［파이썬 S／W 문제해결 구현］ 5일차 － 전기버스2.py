num = int(input())
def elect(idx,cnt):
    global min_val
    if idx+arr[idx] >=n-1:
        min_val = min(min_val, cnt)
    if cnt>=min_val:
        return
    for i in range(arr[idx],0,-1):
        elect(idx + i, cnt + 1)
for seq in range(1,num+1):
    temp = list(map(int,input().split()))
    n = temp[0]
    arr = temp[1:n]
    min_val = 10**9
    elect(0,0)
    print(f'#{seq} {min_val}')