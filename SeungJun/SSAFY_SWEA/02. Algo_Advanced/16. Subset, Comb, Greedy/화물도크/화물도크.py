import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)


# 코드


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    cargo = []
    day = [0] * 25
    cnt = 0
    for _ in range(n):
        s, e = map(int, input().split())
        t = e - s
        cargo.append((s,e,t))
    cargo.sort(key=lambda x: x[2]) # 시간 적은 순으로 정렬
    for c in cargo:
        if not any(day[c[0]:c[1]]): # 해당 시간대가 비어 있으면
            for i in range(c[0],c[1]):
                day[i] = 1
            cnt += 1
        else:
            continue
    print(f'#{tc} {cnt}')

