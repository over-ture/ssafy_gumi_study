import sys
sys.setrecursionlimit(10**6)
n,r,c = map(int,input().split())
def search(n,r,c):
    if n==1:
        cnt = 0
        for x in range(2):
            for y in range(2):
                if x==r and c==y:
                    return cnt
                cnt+=1
    else:
        half  = 2**(n-1)
        if r < half and c < half:
            return search(n-1,r,c)
        elif r < half and c >= half:
            return half*half + search(n-1,r,c-half)
        elif r >= half and c < half:
            return 2*half*half + search(n-1,r-half,c)
        else:
            return 3*half*half + search(n-1,r-half,c-half)
cnt = 0 
result = search(n,r,c)
print(result)
        