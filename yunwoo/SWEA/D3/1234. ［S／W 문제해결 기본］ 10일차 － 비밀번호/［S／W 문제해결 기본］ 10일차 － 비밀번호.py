for seq in range(1, 11):
    n , arr_1 = input().split()
    n = int(n)
    arr = list(arr_1)
    i = 1
    while i <len(arr):
        if arr[i-1]==arr[i]:
            arr.pop(i)
            arr.pop(i-1)
            i -= 1
        else:
            i += 1
    print(f'#{seq} {"".join(arr)}')