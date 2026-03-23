n = int(input())
prod = 1
if n==0:
    prod=1
else:
    for x in range(1,n+1):
        prod*=x
print(prod)