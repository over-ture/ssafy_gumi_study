arr = [[0] * 100 for _ in range(100)]

for _ in range(4):
    x, y, x_1, y_1 = map(int, input().split())
    for i in range(x, x_1):
        for j in range(y, y_1):
            arr[i][j] = 1

result = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            result += 1

print(result)
