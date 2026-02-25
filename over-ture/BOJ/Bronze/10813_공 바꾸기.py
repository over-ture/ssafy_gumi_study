import sys; sys.stdin = open('test.txt')


N, M = map(int, input().split())

arr = []

for i in range(1, N+1):
    arr.append(i)

for c in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    # print(i, j)
    arr[i], arr[j] = arr[j], arr[i]

print(*arr)

