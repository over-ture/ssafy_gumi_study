N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    arr_rev = arr[i-1:j]
    arr_rev.reverse()

    arr[i-1:j] = arr_rev

print(*arr)
