num = int(input())
for seq in range(1, num+1):
    N,M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    max_v = 0
    for i in range(N):
        for j in range(M):
            s = arr[i][j]
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:  # 4방향
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < M:
                    s += arr[ni][nj]
            if max_v < s:
                max_v = s
    print(f'#{seq} {max_v}')
