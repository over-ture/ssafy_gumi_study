a, b = map(int, input().split())
arr = list(map(int,input().split()))
for i in arr:
    if b > i:
        print(i, end=" ")