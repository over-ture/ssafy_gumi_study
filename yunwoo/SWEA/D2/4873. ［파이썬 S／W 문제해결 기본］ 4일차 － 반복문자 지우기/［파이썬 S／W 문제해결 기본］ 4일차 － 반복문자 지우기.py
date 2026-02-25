num = int(input())
for seq in range(1, num+1):
    arr = list(input())
    i = 1
    while i < len(arr):
        if arr[i-1] == arr[i]:
            arr.pop(i)
            arr.pop(i-1)
            i -= 1
        else:
            i += 1
    print(f'#{seq} {len(arr)}')

