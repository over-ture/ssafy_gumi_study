A = [1,2,3,4,5,6,7,8,9,10,11,12]
num = int(input())
def recur(sum_result,start,cnt):
    global result
    if sum_result>k or cnt>n:
        return
    if sum_result == k and cnt == n :
        result += 1
        return
    for i in range(start,12):
        recur(sum_result+A[i],i+1,cnt+1)

for seq in range(1,num+1):
    n,k = map(int,input().split())
    result = 0
    recur(0,0,0)
    print(f'#{seq} {result}')