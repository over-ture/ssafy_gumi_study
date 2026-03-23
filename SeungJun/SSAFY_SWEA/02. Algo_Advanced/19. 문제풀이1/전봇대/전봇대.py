import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

def sol(arr):
    cnt = 0
    hanged = []
    hanged.append((arr[0][0], arr[0][1])) # 처음 전깃줄 매달기
    for s, e in arr[1:]:
        for ps, pe in hanged:
            if s > ps and e > pe or s < ps and e < pe :
                continue
            else: # 걸리면
                cnt += 1
        hanged.append((s,e))
    return cnt

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    hanged = []
    hanged.append((arr[0][0], arr[0][1]))  # 처음 전깃줄 매달기
    for s, e in arr[1:]:
        for ps, pe in hanged:
            if s > ps and e > pe or s < ps and e < pe:
                continue
            else:  # 걸리면
                cnt += 1
        hanged.append((s, e))
    print(f'#{tc} {cnt}')