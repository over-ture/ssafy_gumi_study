import sys; input = sys.stdin.readline
from collections import deque

N, d, k, c = map(int, input().rstrip().split())
conv = [int(input()) for _ in range(N)]

conv += conv[:k-1]

cnt = [0] * (d+1)

curr_type = 0
for i in range(k):
    if cnt[conv[i]] == 0:
        curr_type += 1
    cnt[conv[i]] += 1

max_types = curr_type + (1 if cnt[c] == 0 else 0)

for i in range(N-1):
    cnt[conv[i]] -= 1
    if cnt[conv[i]] == 0:
        curr_type -= 1
    
    if cnt[conv[i+k]] == 0:
        curr_type += 1
    cnt[conv[i+k]] += 1

    tmp_type = curr_type + (1 if cnt[c] == 0 else 0)
    if tmp_type > max_types:
        max_types = tmp_type
    
print(max_types)


