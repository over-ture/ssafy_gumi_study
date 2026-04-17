import sys ; from collections import deque
input = sys.stdin.readline

n = int(input())
inp = list(map(int, input().split()))
b = deque([]) # 풍선s
for i in range(len(inp)):
    b.append((i, inp[i]))
result = []
while b:
    idx, rot = b.popleft()
    result.append(idx+1)
    '''rot가 양수면 왼쪽으로 회전(음수), 음수면 오른쪽으로 회전(양수)
    단, popleft하면서 자동으로 왼쪽으로 한 칸 회전했기 때문에, 
    왼쪽으로 회전할 경우 한 칸 덜 회전해야 함'''
    if rot > 0:
        rot = -rot + 1
    else:
        rot = -rot
    b.rotate(rot)

print(*result)