import sys
input = sys.stdin.readline

scores = [int(input()) for _ in range(10)]

curr = [] # 현재 먹은 버섯 점수

for i in range(10):
    if sum(curr) + scores[i] > 100: # 현재 버섯점수 + 먹을 버섯 점수가 100보다 크다면
        if sum(curr) + scores[i] - 100 > 100 - sum(curr): # 먹었을 때 100점과 점수차가 더 크다면
            print(sum(curr)) # 현재까지 먹은 점수를 출력
            exit()
        else:                                               # 같거나 작다면
            print(sum(curr) + scores[i])                    # 먹었을 때 점수를 출력
            exit()
    else:                      # 현재 버섯점수 + 먹을 버섯 점수가 100보다 작으면
        curr.append(scores[i]) # 그 버섯을 먹는다
print(sum(curr))