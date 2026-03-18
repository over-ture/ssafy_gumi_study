import sys

input = sys.stdin.readline

N = int(input().rstrip())

scores = list(map(int, input().split()))

M = max(scores)

rigged = [x / M * 100 for x in scores]

print(sum(rigged) / len(rigged))