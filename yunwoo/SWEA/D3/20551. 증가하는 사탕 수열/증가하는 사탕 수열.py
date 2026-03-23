num = int(input())
def candy(a,b,c):
    cnt = 0
    while b >= c:
            b -= 1
            cnt += 1
    while a >= b:
        a -= 1
        cnt += 1
    if a < 1 or b <= 1 or c <= 1:
            print(-1)
    else:
        print(cnt)
for seq in range(1,num+1):
    a,b,c = map(int,input().split())
    print(f'#{seq} ',end="")
    candy(a,b,c)
    