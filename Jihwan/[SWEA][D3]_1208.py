def my_min_max(lst): # 최대값, 최대값 인덱스, 최소값, 최소값 인덱스 찾는 함수
    min_v = 100
    max_v = lst[0]
    min_dex = 0
    max_dex = 0

    for i in range(100):
        if max_v <= lst[i]:
            max_v = lst[i]
            max_dex = i
        if min_v >= lst[i]:
            min_v = lst[i]
            min_dex = i
    
    return max_v, max_dex, min_v, min_dex

for t in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    
    while dump > 0: # dump가 0이기 전까지 loop
        max_v, max_dex, min_v, min_dex = my_min_max(boxes)
        boxes[max_dex] -= 1 # 최대값이면 -1
        boxes[min_dex] += 1 # 최소값이면 +1
    
        dump -= 1 # 한번 시행될때마다 dump 횟수 - 1
    
    max_v, _, min_v, _ = my_min_max(boxes) # dump 0일때 최대, 최소값 확인
    print(f'#{t} {max_v - min_v}')