arr = [[0] * 1001 for _ in range(1001)]  # 무식하게풀기

N = int(input())
# result = [0] * (N+1)
for i in range(1, N + 1):
    x, y, w, h = map(int, input().split())
    temp = [i] * w
    for j in arr[y:y+h] : # 각 행에 대하여
        j[x:x+w] = temp

num_index = [0] * (N+1)
for lists in arr : 
    for i in lists :
        num_index[i] += 1

for ans in num_index[1:N+1] :
    print(ans)