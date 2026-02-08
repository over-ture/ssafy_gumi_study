def exp(a,b,c) :
    if b == 0:
        return 1
    
    half_power = exp(a,b//2,c)

    if b % 2 == 0 :
        return (half_power  * half_power ) % c
    else :
        return (half_power * half_power * a) % c
    
a, b, c = map(int, input().split())
    
print(exp(a,b,c))