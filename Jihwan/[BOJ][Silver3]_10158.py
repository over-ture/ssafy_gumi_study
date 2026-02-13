w, h = map(int, input().split()) # 격자 가로, 세로
p, q = map(int, input().split()) # 시작 좌표
t = int(input()) # 시간

pt = (p+t) % (w*2)
qt = (q+t) % (h*2)
x = y = 0

if pt <= w:
    x = pt
else:
    x = 2*w - pt

if qt <= h:
    y = qt
else:
    y = 2*h - qt

print(x, y)