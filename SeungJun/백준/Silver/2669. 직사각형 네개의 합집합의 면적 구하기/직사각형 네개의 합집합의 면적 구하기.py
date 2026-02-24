arr = [[0] * 100 for _ in range(100)]

for _ in range(4) :
    sx, sy, ex, ey = map(int, input().split())
    for i in range(sx, ex) :
        for j in range(sy, ey) :
            arr[i][j] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)