num = int(input())
for seq in range(1,num+1):
    N, K = map(int,input().split())
    arr = [1,2,3,4,5,6,7,8,9,10,11,12]
    n = 12
    count = 0
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        if len(subset) == N and sum(subset)==K :
            count+=1
    print(f'#{seq} {count}')