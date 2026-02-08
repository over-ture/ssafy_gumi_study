num = int(input())
arr = list(map(int, input().split()))
max_val = max(arr)
for i in range(num):
    arr[i] = round(arr[i]/max_val*100,3)
print(f'{sum(arr)/num}')