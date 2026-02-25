import sys; input = sys.stdin.readline

arr = []
j = 0
for _ in range(10):
    i = int(input().rstrip())
    j = i % 42
    arr.append(j)
print(len(set(arr)))
