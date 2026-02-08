max = 0
cnt =0
result =0
for _ in range(9):
    cnt +=1
    a = int(input())
    if a>max:
        max = a
        result = cnt

print(max)
print(result)
