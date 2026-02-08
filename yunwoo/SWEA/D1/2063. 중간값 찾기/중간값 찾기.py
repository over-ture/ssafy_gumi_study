N = int(input())
scores = list(map(int, input().split()))

scores.sort()

print(scores[N // 2])
