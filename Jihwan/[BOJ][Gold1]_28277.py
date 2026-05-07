import sys
input = sys.stdin.readline # 입력 시간 줄임

n, q = map(int, input().split())

parents = {i:i for i in range(1, n+1)}
sets = [set() for _ in range(n+1)]

for i in range(1, n+1):
    s = list(map(int, input().split()))
    sets[i] = set(s[1:])

for j in range(q):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        a, b = query[1], query[2]
        
        # 큰 집합을 a로 
        if len(sets[parents[a]]) < len(sets[parents[b]]):
            parents[a], parents[b] = parents[b], parents[a]
        
        # b는 항상 작은 집합
        for k in sets[parents[b]]:
            sets[parents[a]].add(k)
            
        sets[parents[b]].clear()
        
    else:
        print(len(sets[parents[query[1]]]))
