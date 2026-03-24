from itertools import combinations

def get_dist(h,k): # h = 집 k = 치킨집
    return abs(h[0]-k[0]) + abs(h[1]-k[1])

def get_chicken_dist(comb):
    result = 0
    for h in house: # 각 집에 대하여
        ch_dist = min([get_dist(h,k) for k in comb])
        # 치킨집 중 최소 거리인 치킨집까지의 거리가 치킨 거리
        result += ch_dist
    return result

n, m = map(int, input().split())
arr = []
house = []
kfc = []
ans = float('inf')
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 1:
            house.append((i,j))
        elif temp[j] == 2:
            kfc.append((i,j))
    arr.append(temp)

for comb in combinations(kfc, m):
    if get_chicken_dist(comb) >= ans:
        continue
    else:
        ans = get_chicken_dist(comb)
print(ans)