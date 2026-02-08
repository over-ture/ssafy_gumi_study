T = int(input())

for tc in range(1, T + 1):
    arr = input()
    count = 0
    result = 0
    for i in arr:
        count+=1
    print(f'#{tc}',end =" ")
    for i in range(count//2):
        if arr[i]!= arr[count-i-1]:
            break
    else:
        result = 1
    print(result)

