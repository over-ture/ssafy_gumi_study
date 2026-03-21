S = input().strip()

check_bit = 0
pos = [-1] * 26

for i, char in enumerate(S):
    idx = ord(char) - ord('a')

    if not (check_bit & (1 << idx)):
        pos[idx] = i
        check_bit |= (1 << idx)

print(*pos)