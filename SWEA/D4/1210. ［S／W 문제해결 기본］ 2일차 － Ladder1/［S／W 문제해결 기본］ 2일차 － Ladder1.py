for i in range(10):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    for number in range(100):
        if arr[99][number] == 2 :
            end = number
    i = 99
    j = end
    while i > 0:
        if j > 0 and arr[i][j - 1] == 1:
            while j > 0 and arr[i][j - 1] == 1:
                j -= 1

        elif j < 99 and arr[i][j + 1] == 1:
            while j < 99 and arr[i][j + 1] == 1:
                j += 1
        i -= 1
    print(f'#{num} {j}')

