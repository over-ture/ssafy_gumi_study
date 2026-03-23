n, m = map(int, input().split())

edges = []

if m == 2:
    for i in range(n - 1):
        print(i, i + 1)
    exit()

print(0, 1)
print(1, 2)

for i in range(3, m + 1):
    print(1, i)

for i in range(m + 1, n):
    print(i - 1, i)