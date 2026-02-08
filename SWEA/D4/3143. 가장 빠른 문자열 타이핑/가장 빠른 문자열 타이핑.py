num = int(input())
for seq in range(1,num+1):
    arr, arr_1 = map(str, input().split())
    count = 0
    for _ in arr:
        count+=1

    count_1 = 0
    for _ in arr_1:
        count_1 +=1
    i = 0
    result = 0
    while i<count:
        if arr[i:i+count_1]==arr_1:
            i+=count_1
            result +=1
        else:
            i+=1
    print(f'#{seq} {count-result*(count_1-1)}')


