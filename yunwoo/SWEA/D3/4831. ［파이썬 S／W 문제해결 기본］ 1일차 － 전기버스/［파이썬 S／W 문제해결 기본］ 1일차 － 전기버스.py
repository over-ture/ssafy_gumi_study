num = int(input())
for t in range(1, num + 1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    stop = 0
    result = 0
    idx = 0

    while stop +K < N:
        temp = 0

        if idx < M and stop + K < charge[idx]:
            result = 0
            break

        while idx < M and charge[idx] <= stop + K:
            temp = charge[idx]
            idx += 1

        stop = temp
        result += 1

    print(f'#{t} {result}')
