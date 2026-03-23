import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

def recur(month, total_cost):
    global minimum

    if month > 12:
        minimum = min(minimum, total_cost)
        return

    # 1일권
    recur(month + 1, total_cost + (day[month] * cost_day))
    # 1개월권
    recur(month + 1, total_cost + cost_month)
    # 3개월권
    recur(month + 3, total_cost + cost_month3)
    # 1년권
    recur(month + 12, total_cost + cost_year)


T = int(input())
for tc in range(1,T+1):
    cost_day, cost_month, cost_month3, cost_year = map(int, input().split())
    day = [0] + list(map(int, input().split()))
    minimum = float('inf')
    recur(1,0)

    ans = min(minimum, cost_year)
    print(f'#{tc} {ans}')