arr= input()
i = 0
result = 0
while i<=len(arr)//2:
    if arr[i]!=arr[len(arr)-i-1]:
        break
    i+=1
else:
    result = 1
print(result)