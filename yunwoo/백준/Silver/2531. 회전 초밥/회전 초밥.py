import sys
input = sys.stdin.readline
n,d,k,c = map(int,input().split())
arr = []
for _ in range(n):
    temp = int(input())
    arr.append(temp)
arr.extend(arr[:k-1])
max_val = 0
for x in range(n):
    if len(set(arr[x:x+k]))==k:
        if c not in arr[x:x+k]:
            print(k+1)
            exit()
        else:
            max_val = max(max_val,k)
    else:
        if c not in arr[x:x+k]:
            max_val = max(max_val,len(set(arr[x:x+k]))+1)
        else:
                max_val = max(max_val,len(set(arr[x:x+k])))
print(max_val)