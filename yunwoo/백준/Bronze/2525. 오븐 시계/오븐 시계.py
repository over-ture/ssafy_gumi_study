h,m= map(int,input().split())
mm = int(input())
result = h*60+m+mm
hour = result//60
minute = result%60
if hour>=24:
    hour-=24
print(f'{hour} {minute}')

