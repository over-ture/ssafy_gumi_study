num = int(input())
def post_order(num):
    if num>n:
        return 0 
    left = post_order(num*2)
    right = post_order(num*2+1)
    if left or right:
        value[num] = left + right

    return value[num]

for seq in range(1,num+1):
    n,m,l = map(int,input().split())
    value = [0]*(n+1)
    for _ in range(m):
        num,val = map(int,input().split())
        value[num]=val
    post_order(1)
    print(f'#{seq} {value[l]}')
