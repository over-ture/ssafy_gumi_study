from collections import deque
for _ in range(10):
    seq = int(input())
    arr = list(map(int,input().split()))
    q = deque()
    n = 1
    q.extend(arr[:8])
    print(f'#{seq}',end=" ")
    while True:
        x= q.popleft()
        x-=n
        n = n % 5 + 1
        if x<=0:
            x = 0
            q.append(x)
            print(*q)
            break
        else:
            q.append(x)

