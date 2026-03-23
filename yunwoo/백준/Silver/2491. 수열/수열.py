n = int(input())
arr = list(map(int,input().split()))

temp = 1
result = 1

i = 1
while i < n:
    if arr[i-1] <= arr[i]:
        temp += 1
    else:
        result = max(result, temp)
        temp = 1
    i += 1

result = max(result, temp)   

temp = 1
i = 1
while i < n:
    if arr[i-1] >= arr[i]:
        temp += 1
    else:
        result = max(result, temp)
        temp = 1
    i += 1

result = max(result, temp)  

print(result)