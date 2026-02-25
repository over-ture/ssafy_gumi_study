a,b,c = map(int,input().split())
d = int(input())

total = a*3600 + b*60 + c + d

h = (total // 3600) % 24
m = (total % 3600) // 60
s = total % 60

print(h, m, s)