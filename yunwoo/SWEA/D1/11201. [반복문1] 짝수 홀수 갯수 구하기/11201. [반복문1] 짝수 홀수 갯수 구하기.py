num = int(input())
for seq in range(1,num+1):
    number = int(input())
    arr = list(map(int,input().split()))
    odd = 0
    even = 0
    for i in arr:
        if i%2==0:
            even+=1
        else:
            odd+=1
    print(f'#{seq} {even} {odd}')