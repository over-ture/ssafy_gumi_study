import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)



T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())
    weights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    total = 0

    weights.sort()
    trucks.sort()

    while trucks and weights:
        nw = weights.pop()
        nt = trucks.pop()
        if nt >= nw:
            total += nw
        else:
            trucks.append(nt)
    print(f'#{tc} {total}')
