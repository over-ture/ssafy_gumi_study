import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

def is_it_run(arr):
    for i in range(8):
        if all(arr[i:i+3]):
            return True
    return False

T = int(input())
for tc in range(1,T+1):
    pl1 = [0] * 10
    pl2 = [0] * 10
    winner = 0
    nums = list(map(int, input().split()))
    for i in range(12):
        n = nums[i]
        if i % 2 == 0: #pl1 차례
            pl1[n] += 1
            if is_it_run(pl1) or 3 in pl1:
                winner = 1
                break
        else: #pl2 차례
            pl2[n] += 1
            if is_it_run(pl2) or 3 in pl2:
                winner = 2
                break
    print(f'#{tc} {winner}')
