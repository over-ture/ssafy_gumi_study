import sys ; sys.stdin = open('숫자사각형3_input.txt')


def sol(h, w):
    arr = [[0] * w for _ in range(h)]
    for i in range(h):
        if i % 2 == 0:
            for j in range(w):
                arr[i][j] = i * w + j + 1
        else:
            for j in range(w):
                arr[i][w-1-j] = i * w + j + 1

    for i in range(h):
        for j in range(w):
            print(arr[i][j], end=' ')
        print()



T = int(input())
for tc in range(1,T+1):
    h, w = map(int, input().split())
    print(f'#{tc}')
    sol(h, w)