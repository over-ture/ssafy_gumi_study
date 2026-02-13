T = int(input())

for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    dcs = [1, 0, -1, 0] # 동 남 서 북
    drs = [0, 1, 0, -1]
    
    # 1 = '/'  2 = '\' 
    m1 = [3, 2, 1, 0] # 1번 거울 동 남 서 북에서 올때 dcs, drs 변환 백터
    m2 = [1, 0, 3, 2] # 2번 거울

    c = r = 0 # 초기 0, 0
    move = 0 # 방향
    cnt = 0 # 거울 도달 횟수
    while 0 <= c < n and 0 <= r < n:
        dc = c + dcs[move] # 현재 방향에 따라 다음 방향 위치
        dr = r + drs[move]

        if dc < 0 or dc >= n or dr < 0 or dr >= n:
            break # 다음 위치 인덱스 밖이면 끝
        else:
            c = dc # 인덱스 안이면 이동
            r = dr 
            if arr[r][c] == 1: # 이동 했는데 1번 거울 있으면
                move = m1[move] # 방향 전환
                cnt += 1 # 거울 도달 횟수 + 1
            elif arr[r][c] == 2:
                move = m2[move]
                cnt += 1
        
    print(f'#{t}', cnt)            
