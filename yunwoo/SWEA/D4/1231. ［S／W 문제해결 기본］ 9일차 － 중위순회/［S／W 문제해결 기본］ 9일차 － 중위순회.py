def in_order(T):
    if T:
        in_order(left[T])
        print(value[T],end="")
        in_order(right[T])
for seq in range(1,11):
    N = int(input())
    E = N-1
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    value = [''] * (N + 1)
    for i in range(N):
        arr = input().split()
        p = int(arr[0])
        value[p] = arr[1]
        if len(arr)==4:
            left[p] = int(arr[2])
            right[p] = int(arr[3])
        if len(arr)==3:
            left[p] = int(arr[2])
    print(f'#{seq} ',end="")
    in_order(1)
    print()

