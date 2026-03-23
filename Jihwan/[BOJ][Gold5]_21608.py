dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def step1(num):
    candidate = [[0] * n for _ in range(n)]
    # 후보 칸
    candidate_idx = []
    max_like = 0
    for r in range(n):
        for c in range(n):
            if arr[r][c]: # 이미 앉아있는 곳이면 패스
                continue
            for d in range(4):
                dr = r + dy[d]
                dc = c + dx[d]
                if 0 <= dr < n and 0 <= dc < n:
                    if arr[dr][dc] in like[num]: # 좋아하는 학생 인접 수
                        candidate[r][c] += 1
            max_like = max(candidate[r][c], max_like)
    
    for j in range(n):
        for i in range(n):
            if arr[j][i] == 0 and candidate[j][i] == max_like:
                candidate_idx.append((j, i))
        
    if len(candidate_idx) == 1: # 후보가 하나면 그 자리 배치
        arr[candidate_idx[0][0]][candidate_idx[0][1]] = num
        return
    
    step2(num, candidate_idx) # 후보가 여럿이면 step2로 


def step2(num, candidate):
    candidate_idx = [0] * len(candidate)

    for i in range(len(candidate)):
        r = candidate[i][0]
        c = candidate[i][1]
        for d in range(4):
            dr = r + dy[d]
            dc = c + dx[d]
            if 0 <= dr < n and 0 <= dc < n:
                if arr[dr][dc] == 0:
                    candidate_idx[i] += 1

    max_count = max(candidate_idx) 
    new_cand = []
    if candidate_idx.count(max_count) > 1: # 후보가 또 여러개라면
        for i in range(len(candidate_idx)):
            if candidate_idx[i] == max_count:
                new_cand.append(candidate[i])
        step3(num, new_cand)

    else:
        for i in range(len(candidate_idx)):
            if candidate_idx[i] == max_count:
                arr[candidate[i][0]][candidate[i][1]] = num
                return


def step3(num, candidate):
    candidate.sort()
    arr[candidate[0][0]][candidate[0][1]] = num


n = int(input())
arr = [[0] * n for _ in range(n)] # 교실
like = [[] for _ in range(n**2+1)]

for s in range(n**2):
    student = list(map(int, input().split()))
    std = student[0] # 학생 번호
    like[std] = student[1:] # 각 학생 번호 인덱스에 좋아하는 학생 추가
    step1(std)

ans = 0
for r in range(n):
    for c in range(n):
        cnt = 0
        for d in range(4):
            dr = r + dy[d]
            dc = c + dx[d]
            if 0 <= dr < n and 0 <= dc < n:
                if arr[dr][dc] in like[arr[r][c]]:
                    cnt += 1
        if cnt == 2:
            ans += 10
        elif cnt == 3:
            ans += 100
        elif cnt == 4:
            ans += 1000
        else:
            ans += cnt

print(ans)    