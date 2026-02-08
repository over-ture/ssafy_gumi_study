num  = int(input())
for seq in range(1,num+1):
    number = int(input())
    result=[0]*5001
    for _ in range(number):
        a,b = map(int,input().split())
        for i in range(a,b+1):
            result[i]+=1
    count = int(input())
    ans = [0] * 5001
    for j in range(count):
        bus = int(input())
        ans[j] = result[bus]
    print(f'#{seq}', end=' ')
    for i in range(count):
        print(ans[i], end=' ')
    print()
