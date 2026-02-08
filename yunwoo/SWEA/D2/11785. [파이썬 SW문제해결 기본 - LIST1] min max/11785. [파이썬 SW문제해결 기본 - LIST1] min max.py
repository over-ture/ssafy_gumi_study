a = int(input())
count = 1
for i in range(a):
    n = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[0]
    min_v = arr[0]
    for j in range(1,n):
        if max_v<arr[j]:
            max_v =arr[j]
        if min_v>arr[j]:
            min_v = arr[j]
    print(f'#{count} {max_v-min_v}')
    count +=1