def check_babygin(counts):
    for i in range(10):
        if counts[i] >= 3:
            return True
        if i <= 7:
            if counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
                return True
    return False

T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))

    count_A = [0] * 10
    count_B = [0] * 10
    winner = 0

    for i in range(12):
        card = arr[i]
        
        if i % 2 == 0:
            count_A[card] += 1
            if check_babygin(count_A):
                winner = 1
                break
        else:
            count_B[card] += 1
            if check_babygin(count_B):
                winner = 2
                break

    print(f'#{tc} {winner}')