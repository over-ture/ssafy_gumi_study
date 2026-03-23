import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

def recur(x, y,  total):
    if 0 <= x < N and 0 <= y < N:
        total += arr[x][y]
        if x == N-1 and y == N-1:
            result.append(total)
            return
        if x < N:
            recur(x, y + 1, total)
        if y < N:
            recur(x + 1, y, total)
    return


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    recur(0, 0, 0)
    print(f'#{tc} {min(result)}')