# [로직설계]
# 1. 종료 조건: idx가 N이 되면 깨진 계란의 수를 세고 최댓값을 갱신
# 2. 현재 손에 든 계란이 깨졌거나, 다른 모든 계란이 깨져있다면 idx + 1
# 3. 계란으로 계란치기
#    - 두 계란의 내구도를 각각 상대방의 무게만큼 감소
#    - dfs(idx + 1)을 호출하여 다음 계란
#    - 재귀가 끝나면 감소시켰던 내구도를 다시 복구

import sys
input = sys.stdin.readline

def dfs(idx):
    global max_counts
    
    # 1. 종료 조건: 모든 계란을 다 손에 들어본 경우
    if idx == N:
        counts = 0
        for egg in eggs:
            if egg[0] <= 0:
                counts += 1
        max_counts = max(max_counts, counts)
        return
    
    # 2. 현재 계란이 깨졌거나, 다른 계란이 모두 깨져서 칠 수 없는 경우
    if eggs[idx][0] <= 0:
        dfs(idx + 1)
        return
        
    broken = True
    for i in range(N):
        if i != idx and eggs[i][0] > 0:
            broken = False
            break
            
    if broken:
        dfs(idx + 1)
        return
        
    # 3. 다른 계란과 부딪히기
    for i in range(N):
        if i == idx or eggs[i][0] <= 0:
            continue
            
        eggs[idx][0] -= eggs[i][1]
        eggs[i][0] -= eggs[idx][1]
        dfs(idx + 1)
        eggs[idx][0] += eggs[i][1]
        eggs[i][0] += eggs[idx][1]

# --------------------------------------------------------

N = int(input())

eggs = []   # [계란의 내구도, 무게]
for _ in range(N):
    eggs.append(list(map(int, input().split())))

max_counts = 0
dfs(0)
print(max_counts)
