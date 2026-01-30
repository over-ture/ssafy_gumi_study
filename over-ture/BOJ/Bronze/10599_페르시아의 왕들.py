import sys
input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))


    if nums == [0, 0, 0, 0]:
        break

    # print(min(nums[2:4]) - max(nums[0:2]), end=' ')
    # print(max(nums[2:4]) - min(nums[0:2]))
    min = nums[2] - nums[1]
    max = nums[3] - nums[0]

    print(f'{min} {max}')