import sys ; sys.stdin = open('도로건설input.txt')


def diff_money(road, n):
    total = 0
    middle = sum(road)//n
    for i in road:
        total += abs(i-middle)
    return (middle, total)
    # 다리 하나의 총 건설비용 계산


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    rows = [arr[i] for i in range(n)]  # 가로
    cols = list(map(list, zip(*arr)))  # 세로

    print(f'#{tc}')
    sol(arr, n)