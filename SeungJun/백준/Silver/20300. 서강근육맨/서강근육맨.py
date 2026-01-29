# 20300 서강-근육맨
N = int(input())
muscle_loss = list(map(int, input().split())) # 운동기구별 근손실 리스트
muscle_loss.sort() # 오름차순 정렬
arr = []
if N % 2 == 0 :
    for i in range(len(muscle_loss)) :
        temp  = muscle_loss[i] + muscle_loss[N-1-i]
        arr.append(temp)
else :
    muscle_loss.pop()
    for i in range(len(muscle_loss)) :
        temp  = muscle_loss[i] + muscle_loss[len(muscle_loss)-1-i]
        arr.append(temp)
M = max(arr)
print(M)