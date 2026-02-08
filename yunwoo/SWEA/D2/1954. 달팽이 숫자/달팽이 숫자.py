num = int(input())

for seq in range(1,num+1):
    number = int(input())
    arr = [[0] * number for _ in range(number)]

    di = [0, 1, 0, -1]  # 오른쪽, 아래, 왼쪽, 위
    dj = [1, 0, -1, 0]

    i = j = d = 0
    arr[0][0] = 1

    for num in range(2, number * number + 1):
        ni = i + di[d]
        nj = j + dj[d]

        if 0 <= ni < number and 0 <= nj < number and arr[ni][nj] == 0:
            i, j = ni, nj
        else:
            d = (d + 1) % 4
            i += di[d]
            j += dj[d]

        arr[i][j] = num

    print(f'#{seq}')
    for i in range(number):
        for j in range(number):
            print(arr[i][j], end = " ")
        print()