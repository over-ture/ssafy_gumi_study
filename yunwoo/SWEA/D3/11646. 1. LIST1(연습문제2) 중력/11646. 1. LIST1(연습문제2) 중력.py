a = int(input())
for i in range(1,a+1):
    n = int(input())
    arr = list(map(int, input().split()))
    list_1 =[]
    for j in range(n):
        count = 0
        for q in range(j+1,n):
            if arr[j]>arr[q]:
                count +=1
        list_1.append(count)
    print(f'#{i} {max(list_1)}')