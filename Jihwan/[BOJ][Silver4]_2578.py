arr = [list(map(int, input().split())) for _ in range(5)]
# 빙고판 입력
call = []
# 부르는 콜 리스트

for _ in range(5): 
    x = list(map(int, input().split()))
    call.extend(x) # 5줄의 콜 리스트 extend로 1차원 리스트로 만들기
# 이차원 리스트로 받기 애매할때 extend로 리스트 연장식으로 input 받기!!

def check_bingo(): # 빙고 갯수 확인 함수
    bingo = 0

    for i in range(5): # 가로 직선 빙고 확인
        if arr[i][0:5] == [0] * 5:
            bingo += 1

    for j in range(5): # 세로 직선 빙고 확인
        column = [row[j] for row in arr]
        if column == [0] * 5:
            bingo += 1

    for k in range(5): # 오른쪽 위에서 왼쪽 아래로 대각선 빙고 확인
        if arr[k][4-k] != 0:
            break
    else:
        bingo += 1
    
    for p in range(5): # 왼쪽 위에서 오른쪽 아래로 대각선 빙고 확인
        if arr[p][p] != 0:
            break
    else:
        bingo += 1
    
    return bingo # 빙고 갯수 return

done = False # 3 빙고 되는 순간 멈춤 사인
times = 0 # 콜 몇 번째인지 나타내는 변수 
for c in call:
    times += 1 # 콜 하나 순회마다 + 1
    for row in range(len(arr)): # 빙고판 이중 리스트 인덱스

        # 여기서 len(arr) 나 5안하고 range(row) 돌려서 잘못된 접근으로 시간 낭비했음
        if c in arr[row]: # 콜이 이중 리스트 안에 있다면 
            b = arr[row].index(c) # 해당 콜과 같은 값이 있는 인덱스 확인
            arr[row][b] = 0 # 해당 이중 리스트 내의 인덱스로 그 값 0 만들기

        if check_bingo() >= 3: # 3 빙고 확인
            done = True # 멈춤 사인 on
            break 

    if done: # all break
        print(times) # 몇 번째 콜인지 print
        break