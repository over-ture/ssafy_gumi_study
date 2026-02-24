from collections import deque

num = int(input())
for seq in range(1, num + 1):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))

    for _ in range(m):
        q.append(q.popleft())

    print(f"#{seq} {q[0]}")