num = int(input())
for seq in range(1,num+1):
    n = int(input())
    result = -1
    for x in range(1,10**6+1):
        if x*x*x==n:
            result = x
            break
    print(f'#{seq} {result}')