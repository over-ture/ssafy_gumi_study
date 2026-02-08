num = int(input())
for seq in range(1, num+1):
    start, end = map(int, input().split())
    print(f'#{seq}')
    for j in range(1,10):
        if start <= end:
            for i in range(start,end+1):
                print(f'{i} * {j} = {i*j:2d}',end="   ")
            print()
        elif end < start:
            for i in range(start, end-1,-1):
                print(f'{i} * {j} = {i * j:2d}', end="   ")
            print()


