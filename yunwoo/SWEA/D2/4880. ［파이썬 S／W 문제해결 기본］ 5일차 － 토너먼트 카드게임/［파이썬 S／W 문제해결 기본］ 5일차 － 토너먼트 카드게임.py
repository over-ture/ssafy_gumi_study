num = int(input())
def win(a,b):
    if arr[a]== arr[b]:
        return a
    elif (arr[a]==1 and arr[b]==3) or (arr[a]==2 and arr[b]==1) or(arr[a]==3 and arr[b]==2):
        return a
    else:
        return b
def divide(start,end):
    if start == end:
        return start
    mid = (start + end) // 2
    left = divide(start, mid)
    right = divide(mid+1, end)
    return win(left, right)
for seq in range(1,num+1):
    n = int(input())
    arr = list(map(int, input().split()))
    print(f'#{seq} {divide(0, n - 1) + 1}')