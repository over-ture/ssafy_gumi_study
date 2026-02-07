A = list(map(str, input().rstrip()))
B = list(map(str, input().rstrip()))
# -> 공백으로 나올 수도 있고 공백으로 안나올 수도 있음


pin = 0 # A에서 검색할 시작점 설정
counts = 0 # 등장 횟수
while pin <= len(A) - len(B): # 현재 pin의 값이 (A길이 - B길이) 이하일때만
    if A[pin : pin+len(B)] == B: # A 핀부터 B의 길이만큼이 B랑 같은가?
        counts += 1 # 같으면 +1
        pin += len(B) # 중복이 되면 안되니 pin은 B의 길이만큼 이동
    else: # 다르면
        pin += 1 # pin만 한 칸 이동

print(counts)