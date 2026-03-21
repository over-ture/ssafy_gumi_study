import sys
input = sys.stdin.readline
from collections import deque
n,k = map(int,input().split())
q = deque(i for i in range(1,n+1))
arr = deque(map(int,input().split()))
cnt = 0
result = 0
while result != k:
    if arr[0] == q[0]:
        q.popleft()
        arr.popleft()
        result+=1
    elif q.index(arr[0])<=len(q)//2:
        while q.index(arr[0]) != 0:
            temp  = q.popleft()
            q.append(temp)
            cnt+=1
    else:
        while q.index(arr[0]) != 0:
            temp = q.pop()
            q.appendleft(temp)
            cnt+=1
print(cnt)        




