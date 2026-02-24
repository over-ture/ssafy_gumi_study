import sys ; sys.stdin = open('돌뒤집기input.txt')

def in_range(x):
    global n
    return 0 <= x < n

def sol(i, j):
    for k in range(1,j+1):
        f = i-k # 기준 돌의 앞
        b = i+k # 뒤
        if in_range(f) and in_range(b):
            if arr[f] == arr[b] == 0:
                arr[f] = arr[b] = 1
            elif arr[f] == arr[b] == 1:
                arr[f] = arr[b] = 0
        else:
            break

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(m):
        i, j = map(int, input().split())
        i -= 1
        sol(i, j)
    print(f'#{tc}', end=' ')
    print(*arr)
