def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_max(arr):
    max_val = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > max_val:
                max_val = arr[i][j]

    return max_val

def rotate(arr): # 시계 반대방향 90도 회전
    n = len(arr)
    temp = list(zip(*arr))
    new_arr = []
    for i in range(n-1,-1,-1):
        new_arr.append(temp[i])
    return new_arr

def slide_row(row): # 각 행별 왼쪽으로 밀기
    new_row = []
    temp = [x for x in row if x != 0] # 0 아닌 원소만

    for i in range(len(temp)):
        if temp[i] == 0:
            continue
        if i+1 < len(temp) and temp[i] == temp[i+1]:
            new_row.append(temp[i]*2)
            temp[i+1] = 0
        else:
            new_row.append(temp[i])

    return new_row + [0] * (len(row) - len(new_row))

def slide_all(arr): # 전체 밀기
    nxt_arr = []
    for i in arr:
        nxt_arr.append(slide_row(i))
    return nxt_arr

def main(arr, lv): # 재귀로 분기별 4방향 구현
    if lv == 5:
        max_val = get_max(arr)
        result.append(max_val)
        return

    for i in range(4):
        nxt_arr = slide_all(arr) # 밀고
        main(nxt_arr, lv+1) # 다음단계

        arr = rotate(arr) # 돌리고 다음 턴


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = []
main(arr, 0)
print(max(result))