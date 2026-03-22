# [로직설계]
# rotate 검색해본거
# d.rotate(1)은 맨 뒤 요소를 앞으로, d.rotate(-1)은 맨 앞 요소를 뒤로 보냅니다.

import sys
input = sys.stdin.readline

from collections import deque

# --------------------------------------------------------

N, M = map(int, input().split())
locations = list(map(int, input().split()))

queue = deque(range(1, N + 1))
result = 0
for location in locations:
    idx = queue.index(location)

    if idx <= len(queue) // 2:
        queue.rotate(-idx)
        result += idx
    else:
        queue.rotate(len(queue) - idx)
        result += len(queue) - idx
    queue.popleft()
    
print(result)