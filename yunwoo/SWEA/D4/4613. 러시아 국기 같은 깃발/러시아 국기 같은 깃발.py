T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [input().strip() for _ in range(n)]

    min_val = float('inf')

    # i : W 구간 마지막 줄
    # j : B 구간 마지막 줄
    for i in range(n - 2):
        for j in range(i + 1, n - 1):

            count = 0

            # W 구간
            for x in range(0, i + 1):
                count += m - arr[x].count('W')

            # B 구간
            for x in range(i + 1, j + 1):
                count += m - arr[x].count('B')

            # R 구간
            for x in range(j + 1, n):
                count += m - arr[x].count('R')

            min_val = min(min_val, count)

    print(f"#{tc} {min_val}")