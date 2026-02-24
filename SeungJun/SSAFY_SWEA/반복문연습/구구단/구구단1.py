import sys ; sys.stdin = open('구구단1_input.txt')


def gugudan(s,e):
    if s <= e:
        for i in range(1, 10):
            for j in range(s, e+1):
                print(f'{j} * {i} = {(j*i):2d}', end='   ')
            print()
    else :
        for i in range(1, 10):
            for j in range(s, e-1, -1):
                print(f'{j} * {i} = {(j * i):2d}', end='   ')
            print()
T = int(input())
for tc in range(1,T+1):
    s, e = map(int, input().split())
    print(f'#{tc}')
    gugudan(s, e)