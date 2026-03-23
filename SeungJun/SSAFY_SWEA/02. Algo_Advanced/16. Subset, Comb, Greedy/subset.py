# 부분집합 맨들기(이진 트리에서)
arr = ['O', 'X']
# 세 번 고른다(OOO XXX OXO XOO ...)
# 경우의 수 2개, branch = 2개

path = []
def recur(cnt):
    if cnt == 3:
        print(*path)
        return

    # 매 분기마다 선택
    # O 선택
    path.append(arr[0])
    recur(cnt+1)
    path.pop()

    # X 선택
    path.append(arr[1])
    recur(cnt+1)
    path.pop()
print('-----------부분집합 1(재귀이용)-----------')
recur(0)

# 부분집합 맨들기 2
name = ['MIN', 'CO', 'TIM']
# 가능한 모든 조합은?
def recur2(idx, subset):
    if idx == 3:
        print(*subset)
        return
    # 포함하는경우
    recur2(idx + 1, subset + [name[idx]])
    # 포함안하는경우
    recur2(idx + 1, subset)
print('-----------부분집합 2(재귀이용)-----------')
recur2(0, [])

# 1과 2의 차이
# 2는 원소 포함 여부가 X일때는 그냥 넘김(다음턴으로)
# 그래서 조금 더 효율적

def recur3(cnt):
    if cnt == 3:
        print(*path)
        return

    # cnt번째 인물 포함
    path.append(name[cnt])
    recur3(cnt+1)
    path.pop()

    # cnt번째 인물 미포함
    recur3(cnt+1)

# recur3(0)

# 부분집합 맨들기 3(바이너리 카운팅)
# N개의 비트열을 사용해 각 자리별로 있다 없다 표시
arr = [1, 2, 3, 4]
n = len(arr)

def subet_binary1():
    # 1. 0 ~ 부분 집합의 수만큼 반복
    # -i. 부분집합 번호
    for i in range(1<<n):
        for idx in range(n):
            if i & (1 << idx): # i와 2^idx를 이진으로 표현했을 때, 둘이 1로 겹치는 자릿수가 있다면
                print(arr[idx], end=' ')
        print()

print('-----------부분집합 3(비트연산 이용)-----------')
subet_binary1()