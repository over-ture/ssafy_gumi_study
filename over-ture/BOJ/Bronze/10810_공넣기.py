import sys; sys.stdin = open('test.txt')

N, M = map(int, input().split())
arr = [0] * (N+1)

for t in range(M):
    i, j, k = map(int, input().split())
    for x in range(i-1, j):
        if arr[x] != 0:
            arr[x] = 0
        arr[x] = k
for n in arr[:N]:
    print(n, end=' ')