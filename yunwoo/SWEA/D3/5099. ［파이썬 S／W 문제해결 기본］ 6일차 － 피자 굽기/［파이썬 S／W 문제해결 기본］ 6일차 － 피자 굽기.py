from collections import deque

num = int(input())
for seq in range(1,num+1):
    n, m = map(int,input().split())
    arr = list(map(int,input().split()))
    q = deque()
    for i in range(n):
        q.append((i+1, arr[i]))
    number = n
    while len(q) > 1:
        idx, cheese = q.popleft()
        cheese //= 2
        if cheese == 0:
            if number < m:
                q.append((number + 1, arr[number]))
                number += 1
        else:
            q.append((idx, cheese))
    print(f"#{seq} {q[0][0]}")

