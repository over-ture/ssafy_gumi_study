arr  = []
result = 0
for i in range(10):
    a= int(input())
    arr.append(a)
for i in range(10):
    if arr[i]+result<=100:
        result+=arr[i]
    elif arr[i]+result-100 <=abs(100-result):
        result+=arr[i]
    else:
        break
print(result)