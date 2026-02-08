num = int(input())
for seq in range(1,num+1):
    arr = input()
    arr_1 = input()
    count = 0
    for i in arr:
        count+=1
    n = count
    count_1 = 0
    for j in arr_1:
        count_1+=1
    m = count_1
    length = 0
    result = 0
    print(f'#{seq}',end=" ")
    while length<m-n+1:
        if arr_1[length:length+n] == arr:
            result = 1
            break
        else:
            length += 1 
    print(result)