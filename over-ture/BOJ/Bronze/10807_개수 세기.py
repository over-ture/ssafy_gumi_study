N = int(input())
arr = list(map(int, input().split()))
T = int(input())

cnt = 0
i = 0
while i < N:
    if T == arr[i]:
        cnt += 1
    i += 1
print(cnt)