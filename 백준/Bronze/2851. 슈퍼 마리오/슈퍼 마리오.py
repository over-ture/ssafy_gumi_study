nums = []
for _ in range(10):
    nums.append(int(input()))

total = 0
if sum(nums) < 100 :
        print(sum(nums))
else :
    for i in range(10) :
        curr_total = total
        total += nums[i]

        if total >= 100 :
            a = 100 - curr_total
            b = total - 100
            if a < b:
                print(curr_total)
                break
            else :
                print(total)
                break