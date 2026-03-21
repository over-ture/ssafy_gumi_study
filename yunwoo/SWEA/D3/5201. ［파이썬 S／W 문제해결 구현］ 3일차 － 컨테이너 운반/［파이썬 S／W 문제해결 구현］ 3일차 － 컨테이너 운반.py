num = int(input())
for seq in range(1,num+1):
    n,m = map(int,input().split())
    container = list(map(int,input().split()))
    truck = list(map(int,input().split()))
    container.sort(reverse=True)
    truck.sort(reverse=True)
    i = 0
    j = 0
    result = 0
    while i < len(container) and j < len(truck):
        if container[i] <= truck[j]:
            result += container[i]
            i += 1
            j += 1
        else:
            i += 1
    print(f'#{seq} {result}')