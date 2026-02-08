num = int(input())
cnt = int(input())
result = 0
for _ in range(cnt):
    a, b = map(int,input().split())
    result += a*b
if result == num:
    print("Yes")
else:
    print("No")