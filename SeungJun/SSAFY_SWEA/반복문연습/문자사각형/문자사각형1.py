import sys ; sys.stdin = open('문자사각형1_input.txt')

def al(x):
    if x > 90:
        return x - 90
    else:
        return x
def sol(n):
    arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i][j] = chr(al(65 + i * n +j))

    arr = list(map(list, zip(*arr)))
    for i in range(n):
        for j in range(n):
            print(arr[n-1-i][n-1-j], end=' ')
        print()



T = int(input())
for tc in range(1,T+1):
    n = int(input())
    print(f'#{tc}')
    sol(n)