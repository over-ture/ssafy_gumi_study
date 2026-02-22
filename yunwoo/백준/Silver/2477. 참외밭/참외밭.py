n = int(input())
arr = []
for _ in range(6):
    d, l = map(int, input().split())
    arr.append((d, l))
max_w = 0  
max_h = 0 

for d, l in arr:
    if d in (3, 4):       
        max_w = max(max_w, l)
    else:                 
        max_h = max(max_h, l)

big_area = max_w * max_h

small_area = 0

for i in range(6):
    if arr[i][1] == max_w and arr[(i+1) % 6][1] == max_h:
        small_area = arr[(i+3) % 6][1] * arr[(i+4) % 6][1]
        break
    if arr[i][1] == max_h and arr[(i+1) % 6][1] == max_w:
        small_area = arr[(i+3) % 6][1] * arr[(i+4) % 6][1]
        break

print((big_area - small_area) * n)