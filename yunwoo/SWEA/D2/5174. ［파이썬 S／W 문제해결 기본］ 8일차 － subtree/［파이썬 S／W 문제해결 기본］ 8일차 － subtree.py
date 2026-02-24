num = int(input())
def pre_order(T):
    if T:
        global cnt
        cnt+=1
        pre_order(left[T])
        pre_order(right[T])
for seq in range(1,num+1):
    e,n = map(int,input().split())
    arr = list(map(int,input().split()))
    N = e+1
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    par = [0] * (N + 1)
    cnt = 0
    for i in range(e):
        p,c = arr[i*2],arr[i*2+1]
        par[c]= p
        if left[p]==0:
            left[p]=c
        else:
            right[p]=c
    pre_order(n)
    print(f'#{seq} {cnt}')