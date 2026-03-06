import sys; input = sys.stdin.readline

T = int(input())

for _ in range(T):
    R, S = map(str, input().rstrip().split())
    P = ''

    for i in range(len(S)):
        P += S[i] * int(R)
    
    print(P)