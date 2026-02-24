import sys ; sys.stdin = open('숫자사각형4_input.txt')


def sol(n):
    for i in range(1,n+1):
        for j in range(1, n+1):
            print(i*j, end=' ')
        print()

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    print(f'#{tc}')
    sol(n)