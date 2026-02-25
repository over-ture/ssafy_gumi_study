n = int(input())
white = [[0] * 100 for _ in range(100)]
arr = [list(map(int, input().split())) for _ in range(n)]
for x, y in arr:
    for i in range(x, x+10):
        for j in range(y, y+10):
            white[i][j] = 1
result = 0
for i in range(100):
    for j in range(100):
        if white[i][j]==1:
            result += 1
print(result)
