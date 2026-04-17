import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

def find_set(v):
    if v != team[v]:
        team[v] = find_set(team[v])
    return team[v]

def union(a, b):
    A = find_set(a)
    B = find_set(b)
    if A != B:
        team[B] = A

T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())
    pair = list(map(int,input().split()))
    team = [i for i in range(n+1)]

    cnt = 0
    for i in range(m):
        t1, t2 = pair[i*2], pair[i*2+1]
        union(t1, t2)
    for i in range(1,n+1):
        if team[i] == i:
            cnt += 1
    print(f'#{tc} {cnt}')