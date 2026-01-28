def solution(n) :
    numlist = [0] * 10
    for i in n :
        numlist[int(i)] += 1

    numlist[6] += numlist[9]
    numlist[9] = 0
    numlist[6] = numlist[6] // 2 + numlist[6] % 2

    ans = max(numlist)
    return ans

T = input()
print(solution(T))