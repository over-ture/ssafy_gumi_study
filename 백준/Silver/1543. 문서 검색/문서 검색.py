doc = input()
find = input()
i = 0
cnt = 0

while i < len(doc) :
    if doc[i:i+len(find)] == find :
        cnt += 1
        i += len(find)
    
    else :
        i += 1
        
print(cnt)
        
