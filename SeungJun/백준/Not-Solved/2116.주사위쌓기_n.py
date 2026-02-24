# 2116.주사위 쌓기
T = int(input()) # 주사위 개수

dices = []

for i in range(T) : # T개만큼의 주사위 입력
    new_dice = list(map(int, input().split()))
    dices.append(new_dice)

# 첫 번째 주사위
if dices[0][0] == 6 or dices[0][5] == 6 : # 상하면에 6일 경우

else : # 옆면에 6일 경우
    