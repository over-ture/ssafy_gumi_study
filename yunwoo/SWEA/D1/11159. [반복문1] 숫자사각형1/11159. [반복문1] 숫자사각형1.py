num = int(input())
for seq in range(1,num+1):
    h,w = map(int,input().split())
    count = 1
    print(f'#{seq}')
    for i in range(h):
        for j in range(w):
            print(count, end=" ")
            count+=1
        print()