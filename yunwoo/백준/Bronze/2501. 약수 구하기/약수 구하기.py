num,div = map(int,input().split())
arr=[]
for i in range(1,num+1):
    if num%i==0:
        arr.append(i)
if div>len(arr):
    print(0)
else:
    print(arr[div-1])