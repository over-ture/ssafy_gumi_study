S = int(input())

for cnt in range(1, S+1):
    print(" " * (S - cnt) + "*" * cnt)
