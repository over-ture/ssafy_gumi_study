import sys
sys.stdin = open("test.txt")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []

    for i in range(N):
        arr.append(input())

    result = ""

    for i in range(N):
        for start in range(N - M + 1):
            ok = True
            for k in range(M // 2):
                if arr[i][start + k] != arr[i][start + M - 1 - k]:
                    ok = False
                    break
            if ok:
                result = arr[i][start:start + M]
                break
        if result != "":
            break

    if result == "":
        for j in range(N):
            for start in range(N - M + 1):
                ok = True
                for k in range(M // 2):
                    if arr[start + k][j] != arr[start + M - 1 - k][j]:
                        ok = False
                        break
                if ok:
                    temp = ""
                    for x in range(M):
                        temp += arr[start + x][j]
                    result = temp
                    break
            if result != "":
                break

    print(f"#{tc} {result}")
