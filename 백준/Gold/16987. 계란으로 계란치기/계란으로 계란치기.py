# 계란으로계란치기
def dfs(e, es): # e = 들고잇는계란 t = 때릴계란
    global ans
    
    cnt = 0
    for i in es:
        if i <= 0:
            cnt += 1
    if e == n:
        ans = max(ans, cnt)
        return
    
    if es[e] <= 0 or cnt == n-1 : # 든 계란이 깨졌거나 든 계란 빼고 나머지가 다 깨졌다면
        dfs(e+1, es) # 다음 계란 탐색
        return
    
    for i in range(n):
        if i != e:
            if es[i] <= 0: # 때리려는 계란이 깨져있다면
                continue
            else:
                es[e] -= egg_weight[i] #치고
                es[i] -= egg_weight[e]
                
                dfs(e+1, es)

                es[e] += egg_weight[i] #돌려놓기기
                es[i] += egg_weight[e]

n = int(input())

egg_strength = [] # 계란의내구도
egg_weight = [] # 계란의무게

ans = 0

for i in range(n):
    s, w = map(int, input().split())
    egg_strength.append(s)
    egg_weight.append(w)

dfs(0, egg_strength)
print(ans)