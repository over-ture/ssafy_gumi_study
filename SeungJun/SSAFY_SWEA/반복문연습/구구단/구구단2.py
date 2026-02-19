import sys ; sys.stdin = open('input.txt')

def solution(s,e):
    if s <= e :
        for i in range(s, e+1) :
            for j in range(1,10):
                print(f'{i} * {j} = {(i * j):2d}', end='   ')
                if j == 3 or j == 6 :
                    print('')
            print('\n')
    else :
        for i in range(s, e-1, -1) :
            for j in range(1,10):
                print(f'{i} * {j} = {(i * j):2d}', end='   ')
                if j == 3 or j == 6 :
                    print('')
            print('\n')

T = int(input())
for tc in range(1, T+1) :
    s, e = map(int, input().split())
    print(f'#{tc}')
    solution(s, e)