arr = input()
cnt = [-1] * 26

for i in range(len(arr)):
    if cnt[ord(arr[i]) - 97] == -1:
        cnt[ord(arr[i]) - 97] = i

print(*cnt)