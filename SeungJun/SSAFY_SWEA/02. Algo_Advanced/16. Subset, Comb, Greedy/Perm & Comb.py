# 조합
# 5명중 N명 뽑기
arr = ['A','B','C','D','E']
N = 3
path = []

# N명 중 뽑는다 -> depth는 N
# branch는 5(5명이므로)
def recur(cnt, prev):
    if cnt == N:
        print(path)
        return

    for i in range(prev + 1, len(arr)):
        path.append(arr[i])
        recur(cnt + 1, i)
        path.pop() # path 비우기

# 중복 제거 호출
# recur(0, -1)

# 중복조합
# 이전 선택은 허용, 순서에 다른 중복은 제거
def recur2(cnt, prev):
    if cnt == N:
        print(path)
        return

    for i in range(prev, len(arr)):
        # prev + 1 만 prev로 바꾸면 됨
        path.append(arr[i])
        recur2(cnt + 1, i)
        path.pop() # path 비우기

# 중복 포함 호출
# recur2(0,0)
