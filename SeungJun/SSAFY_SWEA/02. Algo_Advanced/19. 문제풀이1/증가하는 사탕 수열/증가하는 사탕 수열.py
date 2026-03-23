import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

def sol(arr):
    global cnt
    for i in range(1, len(arr)):
        temp = arr[-i] - arr[-(i+1)] # 특정 상자와 바로 앞 상자의 개수 차이(양수면 순증가)
        if temp > 0:
            continue
        else:
            # 개수 차이 + 1개를 먹어야 앞 상자의 개수가 더 적어짐
            arr[-(i + 1)] -= abs(temp) + 1 # 앞 상자에서 꺼내먹기
            cnt += abs(temp) + 1 # 먹은만큼 개수 더하기
    for i in arr:
        if i <= 0:
            cnt = -1
            break

T = int(input())
for tc in range(1,T+1):
    arr = list(map(int, input().split()))
    cnt = 0
    sol(arr)
    # print(arr)
    print(f'#{tc} {cnt}')