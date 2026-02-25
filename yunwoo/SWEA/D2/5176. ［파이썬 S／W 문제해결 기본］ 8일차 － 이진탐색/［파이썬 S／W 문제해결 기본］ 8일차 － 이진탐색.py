def in_order(i):
    global cnt
    if i>N:
        return
    else:
        in_order(i*2)
        tree[i]=cnt
        cnt+=1
        in_order(i*2+1)

num = int(input())
for seq in range(1,num+1):
    N = int(input())
    tree=[0]*(N+1)
    cnt = 1
    in_order(1)
    print(f'#{seq} {tree[1]} {tree[N//2]}')


