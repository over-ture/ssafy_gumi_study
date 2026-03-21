n = int(input())
aa,bb,c,d,e = 0,0,0,0,0
for _ in range(n):
    a,b = map(int,input().split())
    if a==0 or b==0:
        e+=1
    elif a>0 and b>0:
        aa+=1
    elif a<0 and b>0:
        bb+=1
    elif a<0 and b<0:
        c+=1
    else:
        d+=1
print(f"Q1: {aa}")
print(f"Q2: {bb}")
print(f"Q3: {c}")
print(f"Q4: {d}")
print(f"AXIS: {e}")