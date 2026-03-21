arr =list(input().strip())
height = 0
i = 0
while i<len(arr):
    if arr[i]=="(":
        height+=10
        i+=1
        while i<len(arr) and arr[i]=="(" :
            height+=5
            i+=1
    elif arr[i]==")":
        height+=10
        i+=1
        while i<len(arr) and arr[i]==")" :
            height+=5
            i+=1
print(height)