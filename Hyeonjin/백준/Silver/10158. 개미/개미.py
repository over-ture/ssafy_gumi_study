w, h = map(int, input().split())    # 너비, 높이
p, q = map(int, input().split())    # 초기위치 좌표값
t = int(input())                    # 개미 이동 시간

pos_x = (p + t) % (2 * w)
if pos_x > w:
    x = 2 * w - pos_x
else:
    x = pos_x

pos_y = (q + t) % (2 * h)
if pos_y > h:
    y = 2 * h - pos_y
else:
    y = pos_y

print(x, y)