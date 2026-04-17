<<<<<<< HEAD
from collections import deque

n, m = map(int, input().split())
q = deque([])
# 우선순위별 남은 개수 카운트
idx_cnt = [0] * (m + 1)

for _ in range(n):
    p, w = map(int, input().split())
    q.append((p, w))
    idx_cnt[p] += 1

ans = 0
stack = [] 
curr_p = m 

while q:
    p, w = q.popleft()
    
    if p < curr_p:
        q.append((p, w))
        ans += w
    else:
        temp = []
        # 더 가벼운게 위면 밀기
        while stack and stack[-1][0] == p and stack[-1][1] < w:
            top_p, top_w = stack.pop()
            ans += top_w
            temp.append((top_p, top_w))
        
        # 새거 적재
        stack.append((p, w))
        ans += w
        
        # 다시 적재
        while temp:
            top_p, top_w = temp.pop()
            stack.append((top_p, top_w))
            ans += top_w
            
        idx_cnt[p] -= 1
        
        # 현재 우선순위 물건을 다 처리했으면 다음 우선순위로 이동
        while curr_p > 0 and idx_cnt[curr_p] == 0:
            curr_p -= 1

=======
from collections import deque

n, m = map(int, input().split())
q = deque([])
# 우선순위별 남은 개수 카운트
idx_cnt = [0] * (m + 1)

for _ in range(n):
    p, w = map(int, input().split())
    q.append((p, w))
    idx_cnt[p] += 1

ans = 0
stack = [] 
curr_p = m 

while q:
    p, w = q.popleft()
    
    if p < curr_p:
        q.append((p, w))
        ans += w
    else:
        temp = []
        # 더 가벼운게 위면 밀기
        while stack and stack[-1][0] == p and stack[-1][1] < w:
            top_p, top_w = stack.pop()
            ans += top_w
            temp.append((top_p, top_w))
        
        # 새거 적재
        stack.append((p, w))
        ans += w
        
        # 다시 적재
        while temp:
            top_p, top_w = temp.pop()
            stack.append((top_p, top_w))
            ans += top_w
            
        idx_cnt[p] -= 1
        
        # 현재 우선순위 물건을 다 처리했으면 다음 우선순위로 이동
        while curr_p > 0 and idx_cnt[curr_p] == 0:
            curr_p -= 1

>>>>>>> f004f55cad382e72c8c19d5d4be06b3603ab15e3
print(ans)