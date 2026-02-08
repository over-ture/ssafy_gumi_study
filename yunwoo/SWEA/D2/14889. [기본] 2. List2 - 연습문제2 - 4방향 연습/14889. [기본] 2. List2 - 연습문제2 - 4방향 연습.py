import sys
sys.stdin = open("test.txt")

num = int(input())

for seq in range(1,num+1):
    number = int(input())
    list_1 = [list(map(int, input().split())) for _ in range(number)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    result = 0

    for i in range(number):
        for j in range(number):
            b = 0

            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                if 0 <= ni < number and 0 <= nj < number:
                   if (list_1[i][j] - list_1[ni][nj]) >= 0:
                       b += (list_1[i][j] - list_1[ni][nj])
                   else:
                       b-= (list_1[i][j] - list_1[ni][nj])
            result+=b
    print(f'#{seq} {result}')