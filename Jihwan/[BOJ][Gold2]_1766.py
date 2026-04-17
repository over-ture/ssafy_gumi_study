import heapq

def solve():
    solved = [False] * (n+1) # 풀었는지에 대한 여부
    hq = []
    ans = []
    
    # 먼저 풀어야 하는 것이 없는 것부터 시작
    for i in range(1, n+1):
        if cnt[i] == 0:
            heapq.heappush(hq, i)
            solved[i] = True

    while hq:
        problem = heapq.heappop(hq)
        ans.append(problem)
        
        if path[problem]:
            for i in path[problem]: # 이제 풀 수 있는 문제들
                if solved[i]:
                    continue
                
                cnt[i] -= 1 # 퓰어야 할 개수 -1
                
                if cnt[i] == 0 and not solved[i]: # 이제 조건 없이 풀 수 있으면 푸쉬
                    solved[i] = True
                    heapq.heappush(hq, i)
    
    return ans
    

n, m = map(int, input().split())

cnt = {j:0 for j in range(1, n+1)} # 먼저 풀어야 하는 문제 개수
path = {i:[] for i in range(1, n+1)} # 풀면 풀수 있는 문제 리스트

for _ in range(m):
    a, b = map(int, input().split())
    path[a].append(b)
    cnt[b] += 1

print(*solve())