def tilt(arr, dir): # dir : 남 서 북 동 순
    global n
    if dir == 0:
        temp = [[0] * n for _ in range(n)]
        for i in range(n):
            cnt = 0
            for j in range(n):
                if arr[j][i] != 0:
                    temp[cnt] = arr[j][i]
                    cnt += 1
    elif dir == 1:

    elif dir == 2:

    elif dir == 3:


def bomb(arr):
    pass

def recur(board, turn):
    if turn > k:
        return
    gravity = turn % 4

    tilt(board, gravity)

    for i in range(n):
        copied = [row for row in board]
        bomb(copied, gravity, i)
        tilt(copied, gravity)

        min_cnt = min(min_cnt, recur(copied, turn+1))

k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(k):
    arr = tilt(arr, i)
    arr = bomb(arr)

# dys = []
# dxs = []
#
#
# def apply_gravity(board, gravity):
#     for i in range(n):
#         if gravity == 0:
#             y = n - 1
#             x = i
#
#         elif gravity == 1:
#             x = 0
#             y = i
#
#         elif gravity == 2:
#             y = 0
#             x = i
#
#         else:
#             x = n - 1
#             y = i
#
#         y, x로
#         당기기
#
#         for i in range(n):
#             ny = y - dys[g] * i
#             nx = x
#
#
# def explode(copied, gravity, idx):
#     # 폭탄 위치 찾았다.
#
#     "bfs를 이용해서 폭발처리"
#     q = deque()
#     q.push((bomb_y, bomb_x))
#
#     while q:
#         by, bx = q.popleft()
#         copied[by][bx] = 0
#         rng = copied[by][bx] - 1
#
#         for i in range(4):
#             for r in range(rng):
#                 ty = by + dys[i] * r
#                 tx = bx + dxs[i] * r
#
#                 if visited[ty][tx]:
#                     continue
#
#                 visited[ty][tx] = True
#                 q.push((ty, tx))
#
#
# def recur(board, turn):
#     if turn > k:
#         return
#
#     gravity = turn % 4
#
#     apply_gravity(board, gravity)
#
#     min_cnt = n * n
#
#     for i in range(n):
#         copied = [r[:] for r in board]
#
#         explode(copied, gravity, idx)
#         apply_gravity(copied, gravity)
#
#         min_cnt = min(min_cnt, recur(copied, turn + 1))
#
#     return min_cnt

