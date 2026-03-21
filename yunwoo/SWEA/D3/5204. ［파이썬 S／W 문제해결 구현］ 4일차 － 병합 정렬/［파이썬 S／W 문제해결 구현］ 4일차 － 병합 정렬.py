num = int(input())
def merge(left,right):
    global cnt
    result = []
    i,j = 0,0
    if left[len(left)-1]>right[len(right)-1]:
        cnt+=1
    while len(left)>i and len(right)>j:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    left,right = [],[]
    middle = len(arr)//2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left,right)
for seq in range(1,num+1):
    n  = int(input())
    cnt = 0
    temp = list(map(int,input().split()))
    arr = merge_sort(temp)
    print(f'#{seq} {arr[n//2]} {cnt}')