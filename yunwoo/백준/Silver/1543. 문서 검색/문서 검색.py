def count(arr, ans):
    count = 0
    i = 0
    while i<(len(arr)-len(ans)+1):
        if arr[i:i+len(ans)]==ans:
            count+=1
            i+=len(ans)
        else:
            i+=1
    return count 

arr = input()
arr_1 = input()
result = count(arr,arr_1)
print(result)
