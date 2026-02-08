num = int(input())
for seq in range(1, num+1):
    start, end = map(int, input().split())
    print(f'#{seq}')
    for i in range(start,end+1):
        for j in range(1,10):
            print(f'{i} * {j} = {i*j:2d}',end="   ")
            if j ==3 or j==6:
                print()
        print()
        print()
