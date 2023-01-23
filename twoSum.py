nums = [3,3]
target = 6
solution = []
for i in range(len(nums)):
    if (target - nums[i]) in nums and i!=nums.index(target - nums[i]):
        solution.append(i)
        solution.append(nums.index(target - nums[i]))
        break

print(solution) 