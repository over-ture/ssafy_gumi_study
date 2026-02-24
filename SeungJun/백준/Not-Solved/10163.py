arr = [[0] * 1001] * 1001 # 무식하게풀기

N = int(input())
for i in range(1,N+1) :
    x, y, w, h = map(int, input().split())
    
    for j in range(w) :
        arr[y][x + j - 1] = i
    for j in range(h) :
        arr[y + h - 1][x] = i
    
    # 배열의 각 칸의 수는 해당 종이의 순서(1이면 첫번째)
result = []
for i in range(1,N+1) :
    cnt = 0
    for y in arr :
        for x in y :
            if x == i :
                cnt += 1
    result.append(cnt)

print(result)