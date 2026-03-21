arr = ["c=","c-","dz=","d-","lj","nj","s=","z="]
a = list(input())
i = 0
cnt = 0
while True:
    if i==len(a):
        break
    if ''.join(a[i:i+2]) in arr:
        cnt +=1
        i+=2
    elif ''.join(a[i:i+3]) in arr:
        cnt+=1
        i+=3
    else:
        i+=1
        cnt+=1
print(cnt)
