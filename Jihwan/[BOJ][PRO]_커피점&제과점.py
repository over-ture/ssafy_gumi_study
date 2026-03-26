import math
from collections import defaultdict
import heapq

build = defaultdict(list) # 건물번호: [(거리, 도착건물), (거리, 도착건물)]
building = 0 # 빌딩 개수

def dijkstra(shop_lst, r): # 샵에서 모든 집까지 거리
    global building
    float('inf')
    distance = [math.inf] * building
    hq = []
    
    for i in shop_lst:
        distance[i] = 0
        heapq.heappush(hq, (0, i)) # 거리에 출발
    
    while hq:
        dis, cur = heapq.heappop(hq) # 거리, 현재 건물
        if dis > distance[cur]:
            continue
        if dis > r:
            continue
        
        for weight, arrival in build[cur]:
            dist = weight + dis
            if dist < distance[arrival]:
                distance[arrival] = dist
                if dist <= r:
                    heapq.heappush(hq, (dist, arrival))
    
    return distance


def init(N, K, sBuilding, eBuilding, mDistance):
    global building, build
    building = N
    build = defaultdict(list)

    for i in range(K):
        build[sBuilding[i]].append((mDistance[i], eBuilding[i]))
        build[eBuilding[i]].append((mDistance[i], sBuilding[i]))
    return


def add(sBuilding, eBuilding, mDistance): # 새로운 도로 추가
    build[sBuilding].append((mDistance, eBuilding))
    build[eBuilding].append((mDistance, sBuilding))
    return


def calculate(M, mCoffee, P, mBakery, R): # 커피숍 수, 커피숍 id 리스트, 베이커리 수, 베이커리 id 리스트, 제한 거리
    coffee = dijkstra(mCoffee, R)
    bakery = dijkstra(mBakery, R)
    global building
    
    answer = math.inf
    
    for i in range(building): # 주택 순회
        if coffee[i] == 0 or bakery[i] == 0: # 커피숍
            continue
        if coffee[i] > answer or bakery[i] > answer or coffee[i] > R or bakery[i] > R: # 제한거리 넘으면 패스
            continue
        
        sum_distance = coffee[i] + bakery[i]
        answer = min(answer, sum_distance)

    if answer == math.inf:
        return -1
    
    return answer