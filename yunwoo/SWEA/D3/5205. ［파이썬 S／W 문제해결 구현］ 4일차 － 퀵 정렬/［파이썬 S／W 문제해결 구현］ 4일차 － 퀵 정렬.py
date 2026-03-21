num = int(input())
def partition(arr,left,right):
    pivot = arr[left]
    i = left
    j = right
    while i<=j:
        while i<=j and arr[i]<=pivot:
            i+=1
        while i<=j and arr[j]>=pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[left],arr[j]=arr[j],arr[left]
    return j
def quick_sort(arr,left,right):
    if left<right:
        s = partition(arr,left,right)
        quick_sort(arr,left,s-1)
        quick_sort(arr,s+1,right)
        
    

for seq in range(1,num+1):
    n = int(input())
    arr = list(map(int,input().split()))
    quick_sort(arr,0,len(arr)-1)
    print(f'#{seq} {arr[n//2]}')